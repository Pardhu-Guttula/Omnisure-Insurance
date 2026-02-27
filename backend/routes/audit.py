# Epic Title: As a security auditor, I want to perform regular security audits, so that I can identify and mitigate potential security vulnerabilities.

from flask import Blueprint, request, jsonify
from backend.database import get_db_connection
from datetime import datetime
import logging

audit_bp = Blueprint('audit', __name__)

# Logging setup for structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('audit')

@audit_bp.route('/schedule-audit', methods=['POST'])
def schedule_audit():
    scheduled_date = request.json.get('scheduled_date')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Audit (scheduled_date) VALUES (%s)", (scheduled_date,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Audit scheduled successfully'}), 200

@audit_bp.route('/complete-audit', methods=['POST'])
def complete_audit():
    audit_id = request.json.get('audit_id')
    completed_date = datetime.now()
    
    vulnerabilities = request.json.get('vulnerabilities')
    recommendations = request.json.get('recommendations')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Audit SET completed_date = %s WHERE audit_id = %s", (completed_date, audit_id,))
    conn.commit()

    cursor.execute("INSERT INTO Report (audit_id, created_at, vulnerabilities, recommendations) VALUES (%s, %s, %s, %s)",
                   (audit_id, completed_date, vulnerabilities, recommendations))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Audit completed and report generated successfully'}), 200