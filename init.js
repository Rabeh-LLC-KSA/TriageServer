'use strict';

/**
 * One-off importer: loads initial_data/sim.xml (one <log .../> element per line)
 * into the `log` table. Usage: DATABASE_URL=... npm run import
 */
require('dotenv').config();
const fs = require('fs');
const path = require('path');
const readline = require('readline');
const xml2js = require('xml2js');
const { getPool } = require('./lib/db');

const file = process.argv[2] || path.join(__dirname, 'initial_data', 'sim.xml');

async function main() {
  const pool = getPool();
  const rl = readline.createInterface({ input: fs.createReadStream(file), crlfDelay: Infinity });
  let inserted = 0;
  let skipped = 0;

  for await (const line of rl) {
    if (!line.trim().startsWith('<log')) { skipped++; continue; }
    try {
      const result = await xml2js.parseStringPromise(line);
      const a = result.log.$;
      await pool.query('INSERT INTO log VALUES (DEFAULT, $1, $2, $3, $4)', [a.id, a.simstep, a.x, a.y]);
      inserted++;
    } catch (err) {
      skipped++;
      console.error('Skipping line:', err.message);
    }
  }
  console.log(`Imported ${inserted} rows, skipped ${skipped}.`);
  await pool.end();
}

main().catch((err) => { console.error(err); process.exit(1); });
