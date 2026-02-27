# Epic Title: As a policyholder, I want to handle policy renewals in the account management module so that I can renew my policies before they expire.

import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='your_db_host'
    )