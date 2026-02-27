-- Epic Title: Create motor insurance policy schema in PostgreSQL

CREATE TABLE MotorInsurancePolicy (
    policy_id SERIAL PRIMARY KEY,
    vehicle_type VARCHAR(50) NOT NULL,
    premium NUMERIC(10, 2) CHECK (premium > 0) NOT NULL,
    claims_history JSONB NOT NULL,
    policy_holder_name VARCHAR(100) NOT NULL,
    policy_number VARCHAR(50) UNIQUE NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);