# Epic Title: As a data analyst, I want to query and report data using PostgreSQL, so that I can generate accurate and actionable insights.

from flask import Blueprint, request, jsonify
from backend.models.report import Report

report_bp = Blueprint('report', __name__)
reports = []  # In-memory storage for reports

@report_bp.route('/report', methods=['POST'])
def generate_report():
    data = request.get_json()

    content = data.get('content')
    report_id = len(reports) + 1

    if not content:
        return jsonify({'error': 'Report content is required'}), 400

    report = Report(report_id, content)
    reports.append(report)

    return jsonify({'message': 'Report generated successfully', 'report_id': report_id}), 201

@report_bp.route('/report/<int:report_id>', methods=['GET'])
def get_report(report_id):
    report = next((r for r in reports if r.report_id == report_id), None)
    
    if report is None:
        return jsonify({'error': 'Report not found'}), 404

    return jsonify({'report_id': report.report_id, 'content': report.content}), 200