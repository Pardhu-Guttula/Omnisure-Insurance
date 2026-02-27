# Epic Title: As a user, I want to view policy details.

from flask import Flask
from backend.routes.insurance_policy import insurance_policy_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(insurance_policy_bp)

if __name__ == '__main__':
    app.run(debug=True)