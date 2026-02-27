# Epic Title: Password Management

from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.models.otp import OTP
from backend.database import get_db_connection
import smtplib

password_reset_bp = Blueprint('password_reset', __name__)

@password_reset_bp.route('/request_reset', methods=['POST'])
def request_reset():
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM User WHERE email = %s', (email,))
    user_record = cursor.fetchone()
    
    if not user_record:
        return jsonify({'error': 'Account not found'}), 404

    otp = OTP(user_record['id'])
    cursor.execute(
        'INSERT INTO OTP (otp, user_id, expiration) VALUES (%s, %s, %s)',
        (otp.otp, otp.user_id, otp.expiration)
    )
    conn.commit()
    
    # Example email sending (please configure your SMTP server)
    with smtplib.SMTP('localhost') as server:
        server.sendmail(
            'from@example.com',
            email,
            f"Subject: Password Reset OTP\n\nYour OTP is {otp.otp}."
        )
    
    cursor.close()
    conn.close()

    return jsonify({'message': 'Password reset OTP sent successfully'}), 200

@password_reset_bp.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    otp_value = data.get('otp')
    new_password = data.get('new_password')
    
    if not otp_value or not new_password:
        return jsonify({'error': 'OTP and new password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM OTP WHERE otp = %s', (otp_value,))
    otp_record = cursor.fetchone()
    
    if not otp_record or not OTP(**otp_record).is_valid():
        return jsonify({'error': 'Invalid or expired OTP'}), 400

    cursor.execute('SELECT * FROM User WHERE id = %s', (otp_record['user_id'],))
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
    
    cursor.execute('DELETE FROM OTP WHERE otp = %s', (otp_value,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Password reset successfully'}), 200