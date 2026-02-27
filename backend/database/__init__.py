# Epic Title: As a system administrator, I want to implement load balancing strategies, so that the server load is distributed evenly and system availability is improved.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )