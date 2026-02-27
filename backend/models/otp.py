# Epic Title: Password Management

from datetime import datetime, timedelta
from random import randint

class OTP:
    def __init__(self, user_id: int):
        self.otp = self._generate_otp()
        self.user_id = user_id
        self.created_at = datetime.now()
        self.expiration = self.created_at + timedelta(minutes=10)

    def _generate_otp(self) -> str:
        return ''.join([str(randint(0, 9)) for _ in range(6)])

    def is_valid(self) -> bool:
        return datetime.now() < self.expiration