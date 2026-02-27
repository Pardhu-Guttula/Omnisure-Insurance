# Epic Title: User Login using Email and Password

from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.models.session import Session
from backend.database import get_db_connection

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and Password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM User WHERE email = %s', (email,))
    user_record = cursor.fetchone()
    
    if not user_record:
        return jsonify({'error': 'Account not found'}), 404

    user = User(user_record['email'], user_record['password_hash'])
    
    if not user.check_password(password):
        return jsonify({'error': 'Incorrect email or password'}), 400

    session = Session(user_record['id'])
    cursor.execute(
        'INSERT INTO Session (session_id, user_id) VALUES (%s, %s)',
        (session.session_id, session.user_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Login successful', 'session_token': session.session_id}), 200