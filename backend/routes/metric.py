# Epic Title: As an insurer, I want to view interactive dashboards, so that I can get a quick overview of key metrics and actionable insights.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

metric_bp = Blueprint('metric', __name__)

@metric_bp.route('/metrics', methods=['POST'])
def create_metric():
    data = request.get_json()

    dashboard_id = data.get('dashboard_id')
    name = data.get('name')
    value = data.get('value')

    if not dashboard_id or not name or value is None:
        return jsonify({'error': 'Dashboard ID, name, and value are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Metric (dashboard_id, name, value) VALUES (%s, %s, %s)', (dashboard_id, name, value))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'message': 'Metric created successfully'}), 201

@metric_bp.route('/metrics/<int:metric_id>', methods=['GET'])
def get_metric(metric_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM Metric WHERE metric_id = %s', (metric_id,))
    metric = cursor.fetchone()

    if not metric:
        return jsonify({'error': 'Metric not found'}), 404

    cursor.close()
    conn.close()
    
    return jsonify(metric), 200