# Epic Title: As an insurer, I want to view interactive dashboards, so that I can get a quick overview of key metrics and actionable insights.

class Dashboard:
    def __init__(self, dashboard_id: int, title: str, description: str):
        self.dashboard_id = dashboard_id
        self.title = title
        self.description = description