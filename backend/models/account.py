# Epic Title: As a policyholder, I want to view my policy history in the account management module so that I can see my past and current policies.

class Account:
    def __init__(self, account_id: int, username: str, email: str, hashed_password: str):
        self.account_id = account_id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password