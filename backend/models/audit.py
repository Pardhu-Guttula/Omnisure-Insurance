# Epic Title: As a security auditor, I want to perform regular security audits, so that I can identify and mitigate potential security vulnerabilities.

from datetime import datetime

class Audit:
    def __init__(self, audit_id: int, scheduled_date: datetime, completed_date: datetime = None):
        self.audit_id = audit_id
        self.scheduled_date = scheduled_date
        self.completed_date = completed_date