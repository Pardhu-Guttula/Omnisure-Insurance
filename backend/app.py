# Epic Title: As a policyholder, I want to handle policy renewals in the account management module so that I can renew my policies before they expire.

from flask import Flask
from flask_cors import CORS
from backend.routes.policy_history import policy_history_bp
from backend.routes.renewal import renewal_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(policy_history_bp)
app.register_blueprint(renewal_bp)

if __name__ == '__main__':
    app.run(debug=True)