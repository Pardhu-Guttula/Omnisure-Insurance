# Epic Title: As a shopper, I want the system to handle transactions securely using payment gateway APIs.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

transaction_bp = Blueprint('transaction', __name__)

# Mock payment gateway response
def process_payment(details):
    if details.get('card_number') == 'valid_card':
        return {'status': 'success', 'transaction_id': 12345}
    else:
        return {'status': 'failure', 'reason': 'Invalid card details'}

@transaction_bp.route('/process_transaction', methods=['POST'])
def process_transaction():
    try:
        data = request.get_json()
        policy_id = data['policy_id']
        shopper_id = data['shopper_id']
        amount = data['amount']
        payment_details = data['payment_details']

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

            return jsonify({'message': 'Transaction successful', 'transaction_id': transaction_id}), 200
        else:
            return jsonify({'error': 'Transaction failed', 'reason': payment_response['reason']}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500