# Epic Title: As a user, I want to compare insurance policies.

from flask import Blueprint, jsonify, request
from backend.database import get_db_connection

insurance_policy_bp = Blueprint('insurance_policy', __name__)

@insurance_policy_bp.route('/policies', methods=['GET'])
def get_policies():
    try:
        filters = []
        values = []

        premium_min = request.args.get('premium_min', type=float)
        premium_max = request.args.get('premium_max', type=float)
        coverage_min = request.args.get('coverage_min', type=float)
        coverage_max = request.args.get('coverage_max', type=float)
        benefits = request.args.get('benefits', type=str)

        if premium_min is not None:
            filters.append('premium_amount >= %s')
            values.append(premium_min)
        if premium_max is not None:
            filters.append('premium_amount <= %s')
            values.append(premium_max)
        if coverage_min is not None:
            filters.append('coverage_amount >= %s')
            values.append(coverage_min)
        if coverage_max is not None:
            filters.append('coverage_amount <= %s')
            values.append(coverage_max)
        if benefits:
            filters.append('benefits ILIKE %s')
            values.append(f'%{benefits}%')

        query = 'SELECT * FROM InsurancePolicy'
        if filters:
            query += ' WHERE ' + ' AND '.join(filters)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        policies = cursor.fetchall()
        cursor.close()
        conn.close()

        if not policies:
            return jsonify({'message': 'No matching policies found'}), 404

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

@insurance_policy_bp.route('/compare_policies', methods=['POST'])
def compare_policies():
    try:
        data = request.get_json()
        policy_ids = data.get('policy_ids', [])

        if not policy_ids:
            return jsonify({'message': 'No policies selected for comparison'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = 'SELECT * FROM InsurancePolicy WHERE policy_id IN %s'
        cursor.execute(query, (tuple(policy_ids),))
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
        return jsonify({'error': 'Failed to compare policies', 'message': str(e)}), 500

@insurance_policy_bp.route('/clear_comparison', methods=['POST'])
def clear_comparison():
    return jsonify({'message': 'Comparison view cleared'}), 200