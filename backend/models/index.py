# Epic Title: As a database administrator, I want to optimize MySQL database queries and implement proper indexing, so that the overall database performance is improved.

class Index:
    def __init__(self, index_id: int, table_name: str, column_name: str, index_name: str):
        self.index_id = index_id
        self.table_name = table_name
        self.column_name = column_name
        self.index_name = index_name