'use strict';

/**
 * Validates and normalises /path query parameters.
 * Returns { pid, t1, t2 } or throws an Error with status 400.
 */
function parsePathQuery(query) {
  const pid = typeof query.pid === 'string' ? query.pid.trim() : '';
  let t1 = Number.parseInt(query.t1, 10);
  let t2 = Number.parseInt(query.t2, 10);

  const fail = (message) => {
    const err = new Error(message);
    err.status = 400;
    throw err;
  };

  if (!pid || pid.length > 10) fail('pid is required (max 10 characters).');
  if (!Number.isFinite(t1) || !Number.isFinite(t2)) fail('t1 and t2 must be integers.');
  if (t1 > t2) [t1, t2] = [t2, t1]; // numeric swap (previously compared as strings)

  return { pid, t1, t2 };
}

module.exports = { parsePathQuery };
