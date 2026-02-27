# Epic Title: As a user, I want to adhere to secure password policies, so that I can enhance the security of my account.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )