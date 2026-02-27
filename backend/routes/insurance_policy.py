# Epic Title: As a shopper, I want to access a secure online purchasing system using React.

from flask import Blueprint, jsonify, request
from backend.database import get_db_connection

insurance_policy_bp = Blueprint('insurance_policy', __name__)

@insurance_policy_bp.route('/policies', methods=['GET'])
def get_policies():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM InsurancePolicy')
        policies = cursor.fetchall()
        cursor.close()
        conn.close()

        policy_list = []
        for policy in policies:
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
            policy_list.append(policy_obj)

        return jsonify({'policies': policy_list}), 200

    except Exception as e:
        return jsonify({'error': 'Failed to load policies', 'message': str(e)}), 500