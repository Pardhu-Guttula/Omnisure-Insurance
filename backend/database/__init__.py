# Epic Title: As a policyholder, I want secure profile management features in the account management module so that I can update my personal and policy details securely.

import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='your_db_host'
    )