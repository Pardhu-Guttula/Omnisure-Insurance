# Epic Title: As a database administrator, I want to optimize MySQL database queries and implement proper indexing, so that the overall database performance is improved.

class Query:
    def __init__(self, query_id: int, sql_query: str, execution_time: float):
        self.query_id = query_id
        self.sql_query = sql_query
        self.execution_time = execution_time