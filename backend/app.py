# Epic Title: As a data analyst, I want to query and report data using PostgreSQL, so that I can generate accurate and actionable insights.

from flask import Flask
from flask_cors import CORS
from backend.routes.query import query_bp
from backend.routes.report import report_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(query_bp)
app.register_blueprint(report_bp)

if __name__ == '__main__':
    app.run(debug=True)