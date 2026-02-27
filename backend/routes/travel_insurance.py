# Epic Title: Create travel insurance policy schema in PostgreSQL

from flask import Blueprint, request, jsonify
from backend.models.travel_insurance_policy import TravelInsurancePolicy
from backend.database import get_db_connection

travel_insurance_bp = Blueprint('travel_insurance', __name__)

@travel_insurance_bp.route('/create_policy', methods=['POST'])
def create_policy():
    data = request.get_json()
    required_fields = ['policy_holder_name', 'policy_number', 'trip_duration', 'destination', 'coverage_limits', 'start_date', 'end_date']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'All fields are required'}), 400
    
    new_policy = TravelInsurancePolicy(
        policy_holder_name=data['policy_holder_name'],
        policy_number=data['policy_number'],
        trip_duration=data['trip_duration'],
        destination=data['destination'],
        coverage_limits=data['coverage_limits'],
        start_date=data['start_date'],
        end_date=data['end_date']
    )
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO TravelInsurancePolicy (policy_holder_name, policy_number, trip_duration, destination, coverage_limits, start_date, end_date, created_at, updated_at) '
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (new_policy.policy_holder_name, new_policy.policy_number, new_policy.trip_duration, new_policy.destination, new_policy.coverage_limits, new_policy.start_date, new_policy.end_date, new_policy.created_at, new_policy.updated_at)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Policy created successfully'}), 201