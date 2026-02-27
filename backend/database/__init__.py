# Epic Title: OAuth Integration for Social Logins

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_db_user',
        password='your_db_password',
        host='your_db_host',
        database='your_db_name'
    )