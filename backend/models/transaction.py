# Epic Title: As a shopper, I want the system to handle transactions securely using payment gateway APIs.

from datetime import datetime

class Transaction:
    def __init__(self,
                 transaction_id: int,
                 policy_id: int,
                 shopper_id: int,
                 amount: float,
                 status: str,
                 transaction_date: datetime):
        self.transaction_id = transaction_id
        self.policy_id = policy_id
        self.shopper_id = shopper_id
        self.amount = amount
        self.status = status
        self.transaction_date = transaction_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()