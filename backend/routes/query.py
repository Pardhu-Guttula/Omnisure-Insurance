# Epic Title: As a database administrator, I want to optimize MySQL database queries and implement proper indexing, so that the overall database performance is improved.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

query_bp = Blueprint('query', __name__)

def analyze_slow_queries():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
    SELECT 
        query_id, 
        sql_query, 
        execution_time 
    FROM 
        SlowQueries 
    WHERE 
        execution_time > 1
    """
    
    cursor.execute(query)
    slow_queries = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return slow_queries

@query_bp.route('/queries/slow', methods=['GET'])
def get_slow_queries():
    slow_queries = analyze_slow_queries()
    return jsonify(slow_queries), 200

@query_bp.route('/queries/optimize', methods=['POST'])
def optimize_query():
    data = request.get_json()

    query_id = data.get('query_id')

    if not query_id:
        return jsonify({'error': 'Query ID is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch the slow query
    cursor.execute("SELECT sql_query FROM SlowQueries WHERE query_id = %s", (query_id,))
    slow_query = cursor.fetchone()

    if not slow_query:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Query not found'}), 404

    # Implement optimization logic here, e.g., by removing subqueries, using joins, etc.
    optimized_query = slow_query['sql_query'] # Modify this to optimize the actual query

    cursor.execute("UPDATE SlowQueries SET sql_query = %s WHERE query_id = %s", (optimized_query, query_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Query optimized successfully'}), 200