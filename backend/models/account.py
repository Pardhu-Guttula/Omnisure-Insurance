# Epic Title: As a policyholder, I want secure profile management features in the account management module so that I can update my personal and policy details securely.

class Account:
    def __init__(self, account_id: int, username: str, email: str, hashed_password: str):
        self.account_id = account_id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password

    def check_password(self, password: str) -> bool:
        # Placeholder for password check logic
        return True