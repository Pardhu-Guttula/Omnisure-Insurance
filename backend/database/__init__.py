# Epic Title: As an administrator, I want to visualize data using React, so that I can have an interactive and responsive user interface.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )