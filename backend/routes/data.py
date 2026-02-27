# Epic Title: As an administrator, I want to visualize data using React, so that I can have an interactive and responsive user interface.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

data_bp = Blueprint('data', __name__)

@data_bp.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM Data')
    data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(data), 200

@data_bp.route('/data', methods=['POST'])
def add_data():
    data = request.get_json()

    content = data.get('content')

    if not content:
        return jsonify({'error': 'Content is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Data (content) VALUES (%s)', (content,))
    conn.commit()
    
    cursor.close()
    conn.close()

    return jsonify({'message': 'Data added successfully'}), 201

@data_bp.route('/data/<int:data_id>', methods=['PATCH'])
def update_data(data_id):
    data = request.get_json()

    content = data.get('content')

    if not content:
        return jsonify({'error': 'Content is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('UPDATE Data SET content = %s WHERE data_id = %s', (content, data_id))
    conn.commit()
    
    cursor.close()
    conn.close()

    return jsonify({'message': 'Data updated successfully'}), 200

@data_bp.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM Data WHERE data_id = %s', (data_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'message': 'Data deleted successfully'}), 200