# Epic Title: Password Management

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password_hash = self._generate_password_hash(password)
        self.created_at = datetime.now()

    def _generate_password_hash(self, password: str) -> str:
        return generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def set_password(self, password: str):
        self.password_hash = self._generate_password_hash(password)