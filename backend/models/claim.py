# Epic Title: As a policyholder, I want to track my claims in the account management module so that I can see the status and details of my claims.

from datetime import datetime

class Claim:
    def __init__(self,
                 claim_id: int,
                 policy_id: int,
                 account_id: int,
                 amount: float,
                 status: str,
                 date_filed: datetime,
                 resolution: str):
        self.claim_id = claim_id
        self.policy_id = policy_id
        self.account_id = account_id
        self.amount = amount
        self.status = status
        self.date_filed = date_filed
        self.resolution = resolution
        self.created_at = datetime.now()
        self.updated_at = datetime.now()