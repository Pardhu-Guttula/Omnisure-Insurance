# Epic Title: Create travel insurance policy schema in PostgreSQL

from datetime import datetime

class TravelInsurancePolicy:
    def __init__(self,
                 policy_holder_name: str,
                 policy_number: str,
                 trip_duration: int,
                 destination: str,
                 coverage_limits: float,
                 start_date: str,
                 end_date: str):
        self.policy_holder_name = policy_holder_name
        self.policy_number = policy_number
        self.trip_duration = trip_duration
        self.destination = destination
        self.coverage_limits = coverage_limits
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()