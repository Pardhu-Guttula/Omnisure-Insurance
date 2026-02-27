# Epic Title: As a data analyst, I want to query and report data using PostgreSQL, so that I can generate accurate and actionable insights.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
)