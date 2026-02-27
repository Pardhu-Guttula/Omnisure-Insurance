# Epic Title: As a user, I want to enable two-factor authentication, so that I can secure my account with an additional layer of protection.

class Token:
    def __init__(self, user_id: int, otp: str, created_at: str):
        self.user_id = user_id
        self.otp = otp
        self.created_at = created_at