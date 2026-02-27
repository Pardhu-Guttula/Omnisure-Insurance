-- Epic Title: Create life insurance policy schema in PostgreSQL

CREATE TABLE LifeInsurancePolicy (
    policy_id SERIAL PRIMARY KEY,
    policy_holder_name VARCHAR(100) NOT NULL,
    policy_number VARCHAR(50) UNIQUE NOT NULL,
    coverage_amount NUMERIC(12, 2) CHECK (coverage_amount > 0) NOT NULL,
    premium_amount NUMERIC(10, 2) CHECK (premium_amount > 0) NOT NULL,
    beneficiaries JSONB NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);