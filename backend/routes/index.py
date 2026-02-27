# Epic Title: As a database administrator, I want to optimize MySQL database queries and implement proper indexing, so that the overall database performance is improved.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

index_bp = Blueprint('index', __name__)

@index_bp.route('/indexes', methods=['POST'])
def create_index():
    data = request.get_json()

    table_name = data.get('table_name')
    column_name = data.get('column_name')
    index_name = data.get('index_name')

    if not table_name or not column_name or not index_name:
        return jsonify({'error': 'Table name, column name, and index name are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    create_index_query = f"CREATE INDEX {index_name} ON {table_name}({column_name})"
    cursor.execute(create_index_query)
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Index created successfully'}), 201

@index_bp.route('/indexes', methods=['GET'])
def get_indexes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SHOW INDEX FROM YourTableName")
    indexes = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(indexes), 200

@index_bp.route('/indexes', methods=['DELETE'])
def delete_index():
    data = request.get_json()

    table_name = data.get('table_name')
    index_name = data.get('index_name')

    if not table_name or not index_name:
        return jsonify({'error': 'Table name and index name are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    drop_index_query = f"DROP INDEX {index_name} ON {table_name}"
    cursor.execute(drop_index_query)
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Index deleted successfully'}), 200