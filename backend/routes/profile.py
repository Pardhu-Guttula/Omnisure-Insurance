# Epic Title: As a policyholder, I want secure profile management features in the account management module so that I can update my personal and policy details securely.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection
from backend.models.account import Account
import hashlib

profile_bp = Blueprint('profile', __name__)

def verify_authentication(email: str, password: str) -> Account:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Account WHERE email = %s', (email,))
    account_data = cursor.fetchone()
    cursor.close()
    conn.close()

    if not account_data:
        return None
    
    account = Account(account_data[0], account_data[1], account_data[2], account_data[3])
    if not account.check_password(password):
        return None

    return account

@profile_bp.route('/update_profile', methods=['POST'])
def update_profile():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        account = verify_authentication(email, password)
        if not account:
            return jsonify({'error': 'Unauthorized access'}), 401
        
        updated_data = {
            "username": data.get('username'),
            "email": data.get('new_email'),
            "new_password": data.get('new_password')
        }

        conn = get_db_connection()
        cursor = conn.cursor()

        if updated_data["username"]:
            cursor.execute('UPDATE Account SET username = %s WHERE account_id = %s', (updated_data["username"], account.account_id))
        
        if updated_data["email"]:
            cursor.execute('UPDATE Account SET email = %s WHERE account_id = %s', (updated_data["email"], account.account_id))
        
        if updated_data["new_password"]:
            hashed_password = hashlib.sha256(updated_data["new_password"].encode()).hexdigest()
            cursor.execute('UPDATE Account SET hashed_password = %s WHERE account_id = %s', (hashed_password, account.account_id))
        
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Profile updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500