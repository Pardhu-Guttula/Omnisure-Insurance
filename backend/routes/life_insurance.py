# Epic Title: Create life insurance policy schema in PostgreSQL

from flask import Blueprint, request, jsonify
from backend.models.life_insurance_policy import LifeInsurancePolicy
from backend.database import get_db_connection

life_insurance_bp = Blueprint('life_insurance', __name__)

@life_insurance_bp.route('/create_policy', methods=['POST'])
def create_policy():
    data = request.get_json()
    required_fields = ['policy_holder_name', 'policy_number', 'coverage_amount', 'premium_amount', 'beneficiaries', 'start_date', 'end_date']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'All fields are required'}), 400
    
    new_policy = LifeInsurancePolicy(
        policy_holder_name=data['policy_holder_name'],
        policy_number=data['policy_number'],
        coverage_amount=data['coverage_amount'],
        premium_amount=data['premium_amount'],
        beneficiaries=data['beneficiaries'],
        start_date=data['start_date'],
        end_date=data['end_date']
    )
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO LifeInsurancePolicy (policy_holder_name, policy_number, coverage_amount, premium_amount, beneficiaries, start_date, end_date, created_at, updated_at) '
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (new_policy.policy_holder_name, new_policy.policy_number, new_policy.coverage_amount, new_policy.premium_amount, new_policy.beneficiaries, new_policy.start_date, new_policy.end_date, new_policy.created_at, new_policy.updated_at)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Policy created successfully'}), 201