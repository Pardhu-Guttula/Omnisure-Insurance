# Epic Title: As a frontend developer, I want to implement performance optimization techniques for the React frontend, so that it loads faster and provides a smooth user experience.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

asset_bp = Blueprint('asset', __name__)

@asset_bp.route('/assets', methods=['GET'])
def get_assets():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM Asset')
    assets = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(assets), 200

@asset_bp.route('/assets', methods=['POST'])
def create_asset():
    data = request.get_json()

    name = data.get('name')
    path = data.get('path')
    optimized = data.get('optimized', False)

    if not name or not path:
        return jsonify({'error': 'Name and path are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO Asset (name, path, optimized) VALUES (%s, %s, %s)', (name, path, optimized)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Asset created successfully'}), 201

@asset_bp.route('/assets/<int:asset_id>', methods=['PUT'])
def update_asset(asset_id):
    data = request.get_json()
    
    name = data.get('name')
    path = data.get('path')
    optimized = data.get('optimized')

    if not name or not path:
        return jsonify({'error': 'Name and path are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'UPDATE Asset SET name = %s, path = %s, optimized = %s WHERE asset_id = %s',
        (name, path, optimized, asset_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Asset updated successfully'}), 200

@asset_bp.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM Asset WHERE asset_id = %s', (asset_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Asset deleted successfully'}), 200