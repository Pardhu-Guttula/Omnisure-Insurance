# Epic Title: As a shopper, I want to receive digital policy documents after a successful purchase.

from flask import Flask
from flask_cors import CORS
from backend.routes.insurance_policy import insurance_policy_bp
from backend.routes.transaction import transaction_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(insurance_policy_bp)
app.register_blueprint(transaction_bp)

if __name__ == '__main__':
    app.run(debug=True)