# Epic Title: As an insurer, I want to view interactive dashboards, so that I can get a quick overview of key metrics and actionable insights.

class Metric:
    def __init__(self, metric_id: int, dashboard_id: int, name: str, value: float):
        self.metric_id = metric_id
        self.dashboard_id = dashboard_id
        self.name = name
        self.value = value