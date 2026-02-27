# Epic Title: Create life insurance policy schema in PostgreSQL

from datetime import datetime
from typing import List, Dict

class LifeInsurancePolicy:
    def __init__(self,
                 policy_holder_name: str,
                 policy_number: str,
                 coverage_amount: float,
                 premium_amount: float,
                 beneficiaries: List[Dict],
                 start_date: str,
                 end_date: str):
        self.policy_holder_name = policy_holder_name
        self.policy_number = policy_number
        self.coverage_amount = coverage_amount
        self.premium_amount = premium_amount
        self.beneficiaries = beneficiaries
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()