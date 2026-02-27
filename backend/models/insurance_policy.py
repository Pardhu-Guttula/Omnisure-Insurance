# Epic Title: As a shopper, I want to access a secure online purchasing system using React.

from datetime import datetime

class InsurancePolicy:
    def __init__(self,
                 policy_id: int,
                 policy_holder_name: str,
                 policy_number: str,
                 policy_type: str,
                 premium_amount: float,
                 coverage_amount: float,
                 benefits: str,
                 start_date: str,
                 end_date: str):
        self.policy_id = policy_id
        self.policy_holder_name = policy_holder_name
        self.policy_number = policy_number
        self.policy_type = policy_type
        self.premium_amount = premium_amount
        self.coverage_amount = coverage_amount
        self.benefits = benefits
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()