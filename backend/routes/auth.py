# Epic Title: As a user, I want to enable two-factor authentication, so that I can secure my account with an additional layer of protection.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection
import os
import time
import smtplib
import random
from email.mime.text import MIMEText

auth_bp = Blueprint('auth', __name__)

def send_otp_via_email(email: str, otp: str):
    # Using a mocked email sending function. Replace with actual email sending logic.
    sender = 'no-reply@example.com'
    msg = MIMEText(f"Your OTP code is {otp}. It will expire in 5 minutes.")
    msg['Subject'] = 'Your OTP Code'
    msg['From'] = sender
    msg['To'] = email

    # Connect to the server
    try:
        server = smtplib.SMTP('smtp.example.com')
        server.login('user', 'password')
        server.sendmail(sender, [email], msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
    return True

def generate_otp():
    return str(random.randint(100000, 999999))

@auth_bp.route('/enable-2fa', methods=['POST'])
def enable_2fa():
    user_id = request.json.get('user_id')
    method = request.json.get('method')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("UPDATE User SET is_2fa_enabled = 1 WHERE user_id = %s", (user_id,))
    conn.commit()

    cursor.execute("SELECT email, phone FROM User WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()
    
    if method == 'email':
        otp = generate_otp()
        token_expiry = int(time.time()) + 300  # 5 minutes expiry
        send_otp_via_email(user['email'], otp)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Token (user_id, otp, created_at) VALUES (%s, %s, %s)", (user_id, otp, token_expiry))
        conn.commit()
        cursor.close()
        conn.close()
        
    return jsonify({'message': '2FA enabled successfully'}), 200

@auth_bp.route('/login', methods=['POST'])
def login():
    user_id = request.json.get('user_id')
    otp = request.json.get('otp')
    
    # OTP validation logic
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT otp, created_at FROM Token WHERE user_id = %s ORDER BY created_at DESC LIMIT 1", (user_id,))
    token = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if not token:
        return jsonify({'error': 'No OTP found'}), 404
    if otp != token['otp']:
        return jsonify({'error': 'Invalid OTP'}), 400
    if int(time.time()) > int(token['created_at']):
        return jsonify({'error': 'OTP has expired'}), 400

    return jsonify({'message': 'Login successful'}), 200