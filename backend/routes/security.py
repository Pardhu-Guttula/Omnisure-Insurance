# Epic Title: As a user, I want to adhere to secure password policies, so that I can enhance the security of my account.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection
from datetime import datetime, timedelta
import re
import bcrypt

security_bp = Blueprint('security', __name__)

PASSWORD_MIN_LENGTH = 8
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
PASSWORD_EXPIRY_DAYS = 90

def validate_password(password: str) -> str:
    if len(password) < PASSWORD_MIN_LENGTH:
        return 'Password must be at least 8 characters long.'
    if not PASSWORD_REGEX.match(password):
        return 'Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.'
    return ""

@security_bp.route('/validate-password', methods=['POST'])
def validate_password_route():
    data = request.get_json()
    password = data.get('password', '')

    validation_error = validate_password(password)
    if validation_error:
        return jsonify({'error': validation_error}), 400

    return jsonify({'message': 'Password is valid'}), 200

@security_bp.route('/update-password', methods=['POST'])
def update_password_route():
    data = request.get_json()
    user_id = data.get('user_id')
    new_password = data.get('new_password', '')

    validation_error = validate_password(new_password)
    if validation_error:
        return jsonify({'error': validation_error}), 400

    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE User SET password_hash = %s, password_last_changed = %s WHERE user_id = %s",
                   (hashed_password, datetime.now(), user_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Password updated successfully'}), 200

@security_bp.route('/check-password-expiry', methods=['POST'])
def check_password_expiry():
    data = request.get_json()
    user_id = data.get('user_id')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT password_last_changed FROM User WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    password_last_changed = user['password_last_changed']
    if datetime.now() > password_last_changed + timedelta(days=PASSWORD_EXPIRY_DAYS):
        return jsonify({'message': 'Password expired', 'expired': True}), 200

    return jsonify({'message': 'Password is still valid', 'expired': False}), 200