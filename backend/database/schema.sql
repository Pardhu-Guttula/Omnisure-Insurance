-- Epic Title: Store User Credentials Securely in PostgreSQL

CREATE TABLE User (
    id SERIAL PRIMARY KEY,
    email BYTEA NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);