# Epic Title: Create motor insurance policy schema in PostgreSQL

from flask import Blueprint, request, jsonify
from backend.models.motor_insurance_policy import MotorInsurancePolicy
from backend.database import get_db_connection

motor_insurance_bp = Blueprint('motor_insurance', __name__)

@motor_insurance_bp.route('/create_policy', methods=['POST'])
def create_policy():
    data = request.get_json()
    required_fields = ['vehicle_type', 'premium', 'claims_history', 'policy_holder_name', 'policy_number', 'start_date', 'end_date']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'All fields are required'}), 400
    
    new_policy = MotorInsurancePolicy(
        vehicle_type=data['vehicle_type'],
        premium=data['premium'],
        claims_history=data['claims_history'],
        policy_holder_name=data['policy_holder_name'],
        policy_number=data['policy_number'],
        start_date=data['start_date'],
        end_date=data['end_date']
    )
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO MotorInsurancePolicy (vehicle_type, premium, claims_history, policy_holder_name, policy_number, start_date, end_date, created_at, updated_at) '
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (new_policy.vehicle_type, new_policy.premium, new_policy.claims_history, new_policy.policy_holder_name, new_policy.policy_number, new_policy.start_date, new_policy.end_date, new_policy.created_at, new_policy.updated_at)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Policy created successfully'}), 201