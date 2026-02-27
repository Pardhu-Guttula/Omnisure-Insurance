# Epic Title: As a database administrator, I want to optimize MySQL database queries and implement proper indexing, so that the overall database performance is improved.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )