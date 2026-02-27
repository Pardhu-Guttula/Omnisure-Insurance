# Epic Title: As a security auditor, I want to perform regular security audits, so that I can identify and mitigate potential security vulnerabilities.

from flask import Blueprint, jsonify
from backend.database import get_db_connection

report_bp = Blueprint('report', __name__)

@report_bp.route('/reports', methods=['GET'])
def get_reports():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Report")
    reports = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(reports), 200