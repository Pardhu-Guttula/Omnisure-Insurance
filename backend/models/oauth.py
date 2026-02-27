# Epic Title: OAuth Integration for Social Logins

from datetime import datetime

class OAuth:
    def __init__(self, oauth_provider: str, oauth_id: str, user_id: int):
        self.oauth_provider = oauth_provider
        self.oauth_id = oauth_id
        self.user_id = user_id
        self.created_at = datetime.now()