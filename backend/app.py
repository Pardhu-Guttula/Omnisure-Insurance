# Epic Title: As a shopper, I want to access a secure online purchasing system using React.

from flask import Flask
from flask_cors import CORS
from backend.routes.insurance_policy import insurance_policy_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(insurance_policy_bp)

if __name__ == '__main__':
    app.run(debug=True)