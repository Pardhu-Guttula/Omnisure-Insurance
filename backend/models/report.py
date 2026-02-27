# Epic Title: As a security auditor, I want to perform regular security audits, so that I can identify and mitigate potential security vulnerabilities.

class Report:
    def __init__(self, report_id: int, audit_id: int, created_at: datetime, vulnerabilities: str, recommendations: str):
        self.report_id = report_id
        self.audit_id = audit_id
        self.created_at = created_at
        self.vulnerabilities = vulnerabilities
        self.recommendations = recommendations