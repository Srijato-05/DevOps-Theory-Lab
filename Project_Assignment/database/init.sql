-- Init script for PostgreSQL
-- Webapp DB is created natively by the POSTGRES_DB environment variable
-- Here we can add custom extensions or roles

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Auto-create tables on first database boot
CREATE TABLE IF NOT EXISTS records (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);
