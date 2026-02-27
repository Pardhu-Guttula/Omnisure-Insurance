# Epic Title: As a user, I want to adhere to secure password policies, so that I can enhance the security of my account.

from datetime import datetime

class User:
    def __init__(self, user_id: int, username: str, email: str, password_hash: str, password_last_changed: datetime):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.password_last_changed = password_last_changed