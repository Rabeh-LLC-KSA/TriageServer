'use strict';

const express = require('express');
const { getPool } = require('../lib/db');
const { parsePathQuery } = require('../lib/path-query');

const router = express.Router();

/* GET home page. */
router.get('/', (req, res) => {
  res.render('index', { title: 'TriageServer' });
});

router.get('/area', (req, res) => {
  res.send('This is a route for area');
});

/* GET /path?pid=c0&t1=0&t2=1000 — ordered trajectory points for one person. */
router.get('/path', async (req, res, next) => {
  try {
    const { pid, t1, t2 } = parsePathQuery(req.query);
    const { rows } = await getPool().query(
      'SELECT id, pid, time, x, y FROM log WHERE pid = $1 AND time > $2 AND time < $3 ORDER BY time',
      [pid, t1, t2]
    );
    res.json(rows);
  } catch (err) {
    next(err); // previously DB errors left the request hanging
  }
});

module.exports = router;
