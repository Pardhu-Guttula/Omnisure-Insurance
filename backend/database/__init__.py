# Epic Title: As a mobile user, I want the UI to be responsive and mobile-friendly, so that I can access all features comfortably on various mobile devices.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )