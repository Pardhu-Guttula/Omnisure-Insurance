# Epic Title: Store User Credentials Securely in PostgreSQL

from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.config import SECRET_KEY
from backend.database import get_db_connection

user_management_bp = Blueprint('user_management', __name__)

@user_management_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and Password are required'}), 400

    new_user = User(email, password, SECRET_KEY)
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO User (email, password_hash) VALUES (%s, %s)',
                   (new_user.email, new_user.password_hash))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User registered successfully'}), 201

@user_management_bp.route('/change_password', methods=['POST'])
def change_password():
    data = request.get_json()
    user_id = data.get('user_id')
    new_password = data.get('new_password')
    
    if not user_id or not new_password:
        return jsonify({'error': 'User ID and new password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM User WHERE id = %s', (user_id,))
    user_record = cursor.fetchone()
    
    if not user_record:
        return jsonify({'error': 'User not found'}), 404

    user = User(user_record[1], user_record[2], SECRET_KEY)
    user.set_password(new_password)
    
    cursor.execute('UPDATE User SET password_hash = %s WHERE id = %s', 
                   (user.password_hash, user_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Password changed successfully'}), 200