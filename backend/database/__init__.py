# Epic Title: As a data engineer, I want data encryption in the PostgreSQL database, so that sensitive data is protected at rest.

import psycopg2

def get_db_connection():
    return psycopg2.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )