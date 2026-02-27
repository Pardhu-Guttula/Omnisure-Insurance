# Epic Title: As a policyholder, I want to view my policy history in the account management module so that I can see my past and current policies.

from flask import Blueprint, jsonify, request
from backend.database import get_db_connection

policy_history_bp = Blueprint('policy_history', __name__)

@policy_history_bp.route('/policy_history', methods=['GET'])
def get_policy_history():
    account_id = request.args.get('account_id', type=int)
    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM InsurancePolicy WHERE account_id = %s', (account_id,))
    policies = cursor.fetchall()
    cursor.close()
    conn.close()

    if not policies:
        return jsonify({'message': 'No policies found'}), 404

    grouped_policies = {}
    for policy in policies:
        policy_type = policy[4]
        if policy_type not in grouped_policies:
            grouped_policies[policy_type] = []
        policy_obj = {
            'policy_id': policy[0],
            'policy_holder_name': policy[1],
            'policy_number': policy[2],
            'policy_type': policy[3],
            'premium_amount': policy[4],
            'coverage_amount': policy[5],
            'benefits': policy[6],
            'start_date': policy[7],
            'end_date': policy[8],
            'created_at': policy[9],
            'updated_at': policy[10]
        }
        grouped_policies[policy_type].append(policy_obj)

    return jsonify({'policies': grouped_policies}), 200