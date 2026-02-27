# Epic Title: As an insurer, I want to view interactive dashboards, so that I can get a quick overview of key metrics and actionable insights.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboards', methods=['GET'])
def get_dashboards():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM Dashboard')
    dashboards = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return jsonify(dashboards), 200

@dashboard_bp.route('/dashboards', methods=['POST'])
def create_dashboard():
    data = request.get_json()

    title = data.get('title')
    description = data.get('description')

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Dashboard (title, description) VALUES (%s, %s)', (title, description))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Dashboard created successfully'}), 201

@dashboard_bp.route('/dashboard/<int:dashboard_id>', methods=['GET'])
def get_dashboard(dashboard_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM Dashboard WHERE dashboard_id = %s', (dashboard_id,))
    dashboard = cursor.fetchone()

    if not dashboard:
        return jsonify({'error': 'Dashboard not found'}), 404

    cursor.execute('SELECT * FROM Metric WHERE dashboard_id = %s', (dashboard_id,))
    metrics = cursor.fetchall()

    dashboard['metrics'] = metrics

    cursor.close()
    conn.close()

    return jsonify(dashboard), 200