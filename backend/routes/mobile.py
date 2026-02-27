# Epic Title: As a mobile user, I want mobile-specific optimizations, so that I can make use of enhanced mobile functionalities.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

mobile_bp = Blueprint('mobile', __name__)

@mobile_bp.route('/mobile-features', methods=['GET'])
def get_mobile_features():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM MobileFeature WHERE status = "enabled"')
    features = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(features), 200

@mobile_bp.route('/mobile-features', methods=['POST'])
def add_mobile_feature():
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    status = data.get('status')

    if not name or not description or not status:
        return jsonify({'error': 'Name, description, and status are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO MobileFeature (name, description, status) VALUES (%s, %s, %s)", (name, description, status))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Mobile feature added successfully'}), 201

@mobile_bp.route('/mobile-features/<int:feature_id>', methods=['PUT'])
def update_mobile_feature(feature_id):
    data = request.get_json()

    status = data.get('status')

    if not status:
        return jsonify({'error': 'Status is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE MobileFeature SET status = %s WHERE feature_id = %s", (status, feature_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Mobile feature status updated successfully'}), 200