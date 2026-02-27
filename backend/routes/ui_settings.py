# Epic Title: As a mobile user, I want the UI to be responsive and mobile-friendly, so that I can access all features comfortably on various mobile devices.

from flask import Blueprint, jsonify
from backend.database import get_db_connection

ui_settings_bp = Blueprint('ui_settings', __name__)

@ui_settings_bp.route('/ui-settings', methods=['GET'])
def get_ui_settings():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM UISettings')
    settings = cursor.fetchone()

    cursor.close()
    conn.close()

    if settings:
        return jsonify(settings), 200
    else:
        return jsonify({'error': 'UI settings not found'}), 404