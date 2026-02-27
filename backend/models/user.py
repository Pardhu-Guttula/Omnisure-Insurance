# Epic Title: As a user, I want to enable two-factor authentication, so that I can secure my account with an additional layer of protection.

class User:
    def __init__(self, user_id: int, name: str, email: str, phone: str, is_2fa_enabled: bool):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.is_2fa_enabled = is_2fa_enabled