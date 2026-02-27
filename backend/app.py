# Epic Title: As a security auditor, I want to perform regular security audits, so that I can identify and mitigate potential security vulnerabilities.

from flask import Flask
from flask_cors import CORS
from backend.routes.audit import audit_bp
from backend.routes.report import report_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(audit_bp)
app.register_blueprint(report_bp)

if __name__ == '__main__':
    app.run(debug=True)