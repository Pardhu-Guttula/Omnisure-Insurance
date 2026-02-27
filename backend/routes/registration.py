# Epic Title: As a developer, I want to implement the agent onboarding UI using React, so that insurance agents have an intuitive interface to register and onboard.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection
import re

registration_bp = Blueprint('registration', __name__)

def is_valid_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400
    
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Agent (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Registration successful'}), 201