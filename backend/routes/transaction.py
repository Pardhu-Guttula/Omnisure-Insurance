# Epic Title: As a shopper, I want to receive digital policy documents after a successful purchase.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

transaction_bp = Blueprint('transaction', __name__)

# Mock payment gateway response
def process_payment(details):
    if details.get('card_number') == 'valid_card':
        return {'status': 'success', 'transaction_id': 12345}
    else:
        return {'status': 'failure', 'reason': 'Invalid card details'}

def generate_policy_document(policy_id):
    # Generate a mock policy document
    return f"Policy Document for Policy ID: {policy_id}"

def send_email(to_address, subject, body):
    try:
        from_address = "your_email@example.com"
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_address, "your_password")
        
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        
        return True
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        return False

@transaction_bp.route('/process_transaction', methods=['POST'])
def process_transaction():
    try:
        data = request.get_json()
        policy_id = data['policy_id']
        shopper_id = data['shopper_id']
        amount = data['amount']
        payment_details = data['payment_details']
        shopper_email = data['shopper_email']

        # Process payment through payment gateway API
        payment_response = process_payment(payment_details)

        if payment_response['status'] == 'success':
            transaction_id = payment_response['transaction_id']

            # Save transaction to database
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO Transaction (transaction_id, policy_id, shopper_id, amount, status, transaction_date) VALUES (%s, %s, %s, %s, %s, %s)',
                (transaction_id, policy_id, shopper_id, amount, 'completed', datetime.now())
            )
            conn.commit()
            cursor.close()
            conn.close()
            
            # Generate policy document
            policy_document = generate_policy_document(policy_id)

            # Send policy document to shopper's email
            email_sent = send_email(shopper_email, "Your Policy Document", policy_document)

            if not email_sent:
                logging.error(f"Failed to deliver policy document to {shopper_email}")
                return jsonify({'message': 'Transaction successful but failed to send the policy document'}), 500

            return jsonify({'message': 'Transaction successful', 'transaction_id': transaction_id}), 200
        else:
            return jsonify({'error': 'Transaction failed', 'reason': payment_response['reason']}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500