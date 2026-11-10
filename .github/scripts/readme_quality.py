#!/usr/bin/env python3
"""Validate and update RABEH-owned README metadata (Python standard library only)."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
START = "<!-- RABEH:README:START -->"
END = "<!-- RABEH:README:END -->"
REQUIRED = (
    "مع رابح الكل رابح",
    "منصة متكاملة في عالم التقنية المالية حيث تلتقي الفرص بالاستثمار",
    "With RABEH, everyone wins",
    "Your integrated platform in the world of financial technology, where opportunities meet investment.",
    "Marketplace", "Fundraising", "Tokenization", "Exchange",
)

def version_tuple(value):
    if not re.fullmatch(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", value):
        raise ValueError("README version must be MAJOR.MINOR.PATCH")
    return tuple(map(int, value.split(".")))

def metadata(text):
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("expected one README metadata block")
    block = text.split(START, 1)[1].split(END, 1)[0]
    values = {}
    for key, label in (("version", "README version"), ("updated", "Last updated")):
        match = re.search(r"\*\*" + label + r":\*\* `([^`]+)`", block)
        if not match:
            raise ValueError("missing " + label)
        values[key] = match.group(1)
    version_tuple(values["version"])
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", values["updated"]):
        raise ValueError("last-updated date must use YYYY-MM-DD")
    date = dt.date.fromisoformat(values["updated"])
    if date > dt.datetime.now(dt.timezone.utc).date():
        raise ValueError("last-updated date is in the future")
    if not re.search(r"\*\*Last change:\*\* \S", block):
        raise ValueError("missing change summary")
    return values

def outside_fences(text):
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is None:
            lines.append(line)
    if fence:
        raise ValueError("unclosed Markdown code fence")
    return "\n".join(lines)

def check_text(text, path, root):
    info = metadata(text)
    for required in REQUIRED:
        if required not in text:
            raise ValueError("missing brand/pillar text: " + required)
    visible = outside_fences(text)
    for destination in re.findall(r"\[[^\]]*\]\(([^)]+)\)", visible):
        destination = destination.strip().strip("<>").split(" ", 1)[0]
        if not destination or destination.startswith(("#", "//")) or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", destination):
            continue
        destination = unquote(destination.split("#", 1)[0].split("?", 1)[0])
        if destination and not (root / path).parent.joinpath(destination).exists():
            raise ValueError("broken relative link: " + destination)
    if f"| {info['version']} | {info['updated']} |" not in text:
        raise ValueError("current version/date missing from README change log")
    return info

def check_revision(previous, current):
    old, new = metadata(previous), metadata(current)
    if previous != current:
        if version_tuple(new["version"]) <= version_tuple(old["version"]):
            raise ValueError("changed README must increment its documentation version")
        if new["updated"] < old["updated"]:
            raise ValueError("last-updated date must not move backwards")

def update_text(text, version, date, note):
    old = metadata(text)
    version_tuple(version)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise ValueError("date must use YYYY-MM-DD")
    dt.date.fromisoformat(date)
    if version_tuple(version) <= version_tuple(old["version"]):
        raise ValueError("new version must be greater than the current README version")
    if date < old["updated"] or dt.date.fromisoformat(date) > dt.datetime.now(dt.timezone.utc).date():
        raise ValueError("date must be current/past and not older than the last update")
    if not note.strip() or any(c in note for c in "\r\n|"):
        raise ValueError("use a nonempty, single-line change summary without table separators")
    left, rest = text.split(START, 1)
    block, right = rest.split(END, 1)
    block = re.sub(r"(\*\*README version:\*\* `)[^`]+(`)", lambda m: m[1] + version + m[2], block)
    block = re.sub(r"(\*\*Last updated:\*\* `)[^`]+(`)", lambda m: m[1] + date + m[2], block)
    block = re.sub(r"\*\*Last change:\*\* [^\n]+", lambda _: "**Last change:** " + note.strip(), block)
    result = left + START + block + END + right
    table = "| Version | Date | Changes |\n| --- | --- | --- |\n"
    if result.count(table) != 1:
        raise ValueError("expected one standard README change log table")
    return result.replace(table, table + f"| {version} | {date} | {note.strip()} |\n", 1)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--base-ref", default=os.getenv("README_BASE_SHA", ""))
    parser.add_argument("--update", metavar="README_PATH")
    parser.add_argument("--version")
    parser.add_argument("--date", default=dt.datetime.now(dt.timezone.utc).date().isoformat())
    parser.add_argument("--note")
    args = parser.parse_args()
    manifest = json.loads((ROOT / ".github/readme-manifest.json").read_text(encoding="utf-8"))
    paths = manifest["readmes"]
    if args.update:
        if args.update not in paths or not args.version or not args.note:
            parser.error("--update requires a managed README path, --version and --note")
        target = ROOT / args.update
        updated = update_text(target.read_text(encoding="utf-8"), args.version, args.date, args.note)
        check_text(updated, args.update, ROOT)
        target.write_text(updated, encoding="utf-8")
        print("Updated " + args.update)
        return
    errors = []
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    discovered = {p for p in tracked if re.fullmatch(r"readme(?:\.[^/]*)?", Path(p).name, re.I)}
    allowed = set(paths) | set(manifest.get("excluded", {}))
    for path in sorted(discovered - allowed):
        errors.append(path + ": add this README to the manifest or document its third-party exclusion")
    if set(paths) - discovered:
        errors.append("managed README missing from git: " + ", ".join(sorted(set(paths) - discovered)))
    for path in paths:
        try:
            current = (ROOT / path).read_text(encoding="utf-8")
            check_text(current, path, ROOT)
            if args.base_ref:
                previous = subprocess.run(["git", "show", f"{args.base_ref}:{path}"], cwd=ROOT, capture_output=True, text=True)
                if previous.returncode == 0 and START in previous.stdout:
                    check_revision(previous.stdout, current)
        except (OSError, ValueError) as exc:
            errors.append(path + ": " + str(exc))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"Validated {len(paths)} RABEH READMEs: brand, pillars, metadata, links and change history.")

if __name__ == "__main__":
    main()
