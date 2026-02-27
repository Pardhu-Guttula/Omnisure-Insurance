# Epic Title: OAuth Integration for Social Logins

from datetime import datetime
from uuid import uuid4

class Session:
    def __init__(self, user_id: int):
        self.session_id = str(uuid4())
        self.user_id = user_id
        self.created_at = datetime.now()