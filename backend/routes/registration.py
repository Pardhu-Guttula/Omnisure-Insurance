# Epic Title: User Registration using Email and Password

from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.database import get_db_connection

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and Password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User WHERE email = %s', (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        return jsonify({'error': 'Duplicate email'}), 400

    if len(password) < 8:  # Simplistic password complexity check
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    new_user = User(email, password)

    cursor.execute(
        'INSERT INTO User (email, password_hash) VALUES (%s, %s)',
        (new_user.email, new_user.password_hash)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User registered successfully'}), 201