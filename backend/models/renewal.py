# Epic Title: As a policyholder, I want to handle policy renewals in the account management module so that I can renew my policies before they expire.

from datetime import datetime

class Renewal:
    def __init__(self, renewal_id: int, policy_id: int, renewal_date: datetime, status: str):
        self.renewal_id = renewal_id
        self.policy_id = policy_id
        self.renewal_date = renewal_date
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()