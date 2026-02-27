# Epic Title: As a mobile user, I want the UI to be responsive and mobile-friendly, so that I can access all features comfortably on various mobile devices.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM User')
    users = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(users), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM User WHERE user_id = %s', (user_id,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404