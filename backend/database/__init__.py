# Epic Title: As a mobile user, I want mobile-specific optimizations, so that I can make use of enhanced mobile functionalities.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )