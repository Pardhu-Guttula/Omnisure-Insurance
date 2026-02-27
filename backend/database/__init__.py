# Epic Title: As an insurer, I want to view interactive dashboards, so that I can get a quick overview of key metrics and actionable insights.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )