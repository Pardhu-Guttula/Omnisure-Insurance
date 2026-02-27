# Epic Title: Create motor insurance policy schema in PostgreSQL

from datetime import datetime
from typing import List, Dict

class MotorInsurancePolicy:
    def __init__(self,
                 vehicle_type: str,
                 premium: float,
                 claims_history: List[Dict],
                 policy_holder_name: str,
                 policy_number: str,
                 start_date: str,
                 end_date: str):
        self.vehicle_type = vehicle_type
        self.premium = premium
        self.claims_history = claims_history
        self.policy_holder_name = policy_holder_name
        self.policy_number = policy_number
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()