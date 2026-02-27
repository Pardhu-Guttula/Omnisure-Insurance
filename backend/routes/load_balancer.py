# Epic Title: As a system administrator, I want to implement load balancing strategies, so that the server load is distributed evenly and system availability is improved.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection

load_balancer_bp = Blueprint('load_balancer', __name__)

current_index = 0

@load_balancer_bp.route('/load-balancer/distribute', methods=['GET'])
def distribute_traffic():
    global current_index

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM ServerInstance WHERE status = 'active'")
    active_instances = cursor.fetchall()

    if not active_instances:
        return jsonify({'error': 'No active server instances'}), 503

    selected_instance = active_instances[current_index]
    current_index = (current_index + 1) % len(active_instances)

    cursor.close()
    conn.close()

    return jsonify({'redirect_to': selected_instance['address']}), 200

@load_balancer_bp.route('/load-balancer/monitor', methods=['GET'])
def monitor_performance():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM ServerInstance")
    instances = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(instances), 200

@load_balancer_bp.route('/load-balancer/update-status', methods=['POST'])
def update_status():
    data = request.get_json()

    instance_id = data.get('instance_id')
    status = data.get('status')

    if not instance_id or not status:
        return jsonify({'error': 'Instance ID and status are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE ServerInstance SET status = %s WHERE instance_id = %s", (status, instance_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Server instance status updated successfully'}), 200