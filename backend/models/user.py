# Epic Title: Store User Credentials Securely in PostgreSQL

from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from datetime import datetime

class User:
    def __init__(self, email: str, password: str, key: bytes):
        self.email = self._encrypt_email(email, key)
        self.password_hash = self._generate_password_hash(password)
        self.created_at = datetime.now()

    def _generate_password_hash(self, password: str) -> str:
        return generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def _encrypt_email(self, email: str, key: bytes) -> bytes:
        fernet = Fernet(key)
        return fernet.encrypt(email.encode())

    def _decrypt_email(self, encrypted_email: bytes, key: bytes) -> str:
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_email).decode()

    def set_password(self, password: str):
        self.password_hash = self._generate_password_hash(password)

    def set_email(self, email: str, key: bytes):
        self.email = self._encrypt_email(email, key)