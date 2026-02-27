# Epic Title: Password Management

from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.database import get_db_connection

change_password_bp = Blueprint('change_password', __name__)

@change_password_bp.route('/change_password', methods=['POST'])
def change_password():
    data = request.get_json()
    session_token = data.get('session_token')
    new_password = data.get('new_password')
    
    if not session_token or not new_password:
        return jsonify({'error': 'Session token and new password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Session WHERE session_id = %s', (session_token,))
    session_record = cursor.fetchone()
    
    if not session_record:
        return jsonify({'error': 'Invalid session'}), 400

    cursor.execute('SELECT * FROM User WHERE id = %s', (session_record['user_id'],))
    user_record = cursor.fetchone()
    
    if not user_record:
        return jsonify({'error': 'User not found'}), 404

    user = User(user_record['email'], user_record['password_hash'])
    user.set_password(new_password)
    
    cursor.execute(
        'UPDATE User SET password_hash = %s WHERE id = %s',
        (user.password_hash, user_record['id'])
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Password changed successfully'}), 200