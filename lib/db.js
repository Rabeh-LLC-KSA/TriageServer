'use strict';

/**
 * Shared PostgreSQL connection pool.
 * Configuration comes only from the environment — never commit credentials.
 *   DATABASE_URL=postgres://user:password@host:5432/dbname
 */
const { Pool } = require('pg');

let pool;

function getPool() {
  if (!pool) {
    if (!process.env.DATABASE_URL) {
      throw new Error('DATABASE_URL is not set. Copy .env.example to .env and configure it.');
    }
    pool = new Pool({
      connectionString: process.env.DATABASE_URL,
      max: Number(process.env.PG_POOL_MAX || 10),
      idleTimeoutMillis: 30000,
    });
  }
  return pool;
}

module.exports = { getPool };
