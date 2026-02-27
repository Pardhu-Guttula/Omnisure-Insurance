# Epic Title: As a user, I want to enable two-factor authentication, so that I can secure my account with an additional layer of protection.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )