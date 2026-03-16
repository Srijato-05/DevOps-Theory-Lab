-- Init script for PostgreSQL
-- Webapp DB is created natively by the POSTGRES_DB environment variable
-- Here we can add custom extensions or roles

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Additional setup can be performed here if necessary
