# Epic Title: As a system architect, I want to implement caching strategies in both frontend and backend, so that the system can handle a larger number of requests efficiently.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )