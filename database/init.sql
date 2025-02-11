-- Create database
DROP TABLE IF EXISTS economic_memory CASCADE;
DROP TABLE IF EXISTS hacker_memory CASCADE;
DROP TABLE IF EXISTS poet_memory CASCADE;
DROP TABLE IF EXISTS religious_philosophical_memory CASCADE;

-- Connect to the database
\c vms_data;

-- Table for economic memory
CREATE TABLE IF NOT EXISTS economic_memory (
    id SERIAL PRIMARY KEY,
    vector_id TEXT UNIQUE NOT NULL,
    source_text TEXT,
    metadata JSONB
);

-- Table for hacker memory
CREATE TABLE IF NOT EXISTS hacker_memory (
    id SERIAL PRIMARY KEY,
    vector_id TEXT UNIQUE NOT NULL,
    source_text TEXT,
    metadata JSONB
);

-- Table for poet memory
CREATE TABLE IF NOT EXISTS poet_memory (
    id SERIAL PRIMARY KEY,
    vector_id TEXT UNIQUE NOT NULL,
    source_text TEXT,
    metadata JSONB
);

-- Table for religious and philosophical memory 
CREATE TABLE IF NOT EXISTS religious_philosophical_memory (
    id SERIAL PRIMARY KEY,
    vector_id TEXT UNIQUE NOT NULL,
    source_text TEXT,
    metadata JSONB
);