# Epic Title: As a developer, I want to implement the agent onboarding UI using React, so that insurance agents have an intuitive interface to register and onboard.

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='your_user',
        password='your_password',
        host='your_host',
        database='your_database'
    )