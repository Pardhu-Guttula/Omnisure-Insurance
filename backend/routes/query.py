# Epic Title: As a data analyst, I want to query and report data using PostgreSQL, so that I can generate accurate and actionable insights.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

query_bp = Blueprint('query', __name__)

@query_bp.route('/query', methods=['POST'])
def execute_query():
    data = request.get_json()

    query_string = data.get('query_string')

    if not query_string:
        return jsonify({'error': 'Query string is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(query_string)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(results), 200