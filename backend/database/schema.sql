-- Epic Title: Create travel insurance policy schema in PostgreSQL

CREATE TABLE TravelInsurancePolicy (
    policy_id SERIAL PRIMARY KEY,
    policy_holder_name VARCHAR(100) NOT NULL,
    policy_number VARCHAR(50) UNIQUE NOT NULL,
    trip_duration INT CHECK (trip_duration > 0) NOT NULL,
    destination VARCHAR(255) NOT NULL,
    coverage_limits NUMERIC(10, 2) CHECK (coverage_limits > 0) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);