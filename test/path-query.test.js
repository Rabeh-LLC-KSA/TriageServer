'use strict';
const test = require('node:test');
const assert = require('node:assert');
const { parsePathQuery } = require('../lib/path-query');

test('swaps t1/t2 numerically, not as strings', () => {
  // As strings "9" > "10"; numerically no swap is needed.
  assert.deepStrictEqual(parsePathQuery({ pid: 'c0', t1: '9', t2: '10' }), { pid: 'c0', t1: 9, t2: 10 });
  assert.deepStrictEqual(parsePathQuery({ pid: 'c0', t1: '100', t2: '5' }), { pid: 'c0', t1: 5, t2: 100 });
});

test('rejects missing pid and non-numeric times with 400', () => {
  assert.throws(() => parsePathQuery({ t1: '1', t2: '2' }), (e) => e.status === 400);
  assert.throws(() => parsePathQuery({ pid: 'c0', t1: 'a', t2: '2' }), (e) => e.status === 400);
  assert.throws(() => parsePathQuery({ pid: 'x'.repeat(11), t1: '1', t2: '2' }), (e) => e.status === 400);
});

test('app boots and serves / without a database', async () => {
  const app = require('../app');
  const server = app.listen(0);
  const { port } = server.address();
  const res = await fetch(`http://127.0.0.1:${port}/`);
  assert.strictEqual(res.status, 200);
  const bad = await fetch(`http://127.0.0.1:${port}/path?t1=1&t2=2`);
  assert.strictEqual(bad.status, 400);
  server.close();
});
