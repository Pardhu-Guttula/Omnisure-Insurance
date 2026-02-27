# Epic Title: As a policyholder, I want to handle policy renewals in the account management module so that I can renew my policies before they expire.

from flask import Blueprint, jsonify, request
from backend.database import get_db_connection
from backend.models.renewal import Renewal

renewal_bp = Blueprint('renewal', __name__)

@renewal_bp.route('/renewals', methods=['GET'])
def get_renewals():
    account_id = request.args.get('account_id', type=int)
    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM InsurancePolicy WHERE account_id = %s AND end_date > %s AND status = %s', (account_id, datetime.now(), 'eligible'))
    policies = cursor.fetchall()
    cursor.close()
    conn.close()

    if not policies:
        return jsonify({'message': 'No policies eligible for renewal'}), 404

    policy_list = []
    for policy in policies:
        policy_list.append({
            'policy_id': policy[0],
            'policy_holder_name': policy[1],
            'policy_number': policy[2],
            'policy_type': policy[3],
            'premium_amount': policy[4],
            'coverage_amount': policy[5],
            'benefits': policy[6],
            'start_date': policy[7],
            'end_date': policy[8],
            'status': policy[9]
        })

    return jsonify({'policies': policy_list}), 200

@renewal_bp.route('/renew', methods=['POST'])
def renew_policy():
    try:
        data = request.get_json()
        policy_id = data['policy_id']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM InsurancePolicy WHERE policy_id = %s AND status = %s', (policy_id, 'eligible'))
        policy = cursor.fetchone()

        if not policy:
            cursor.close()
            conn.close()
            return jsonify({'error': 'Policy not eligible for renewal'}), 400

        new_end_date = policy[8] + timedelta(days=365)
        cursor.execute('UPDATE InsurancePolicy SET end_date = %s, updated_at = %s WHERE policy_id = %s', (new_end_date, datetime.now(), policy_id))
        
        renewal = Renewal(renewal_id=None, policy_id=policy_id, renewal_date=datetime.now(), status='completed')
        cursor.execute('INSERT INTO Renewal (policy_id, renewal_date, status) VALUES (%s, %s, %s)', (renewal.policy_id, renewal.renewal_date, renewal.status))
        
        cursor.close()
        conn.commit()
        conn.close()

        return jsonify({'message': 'Policy renewed successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500