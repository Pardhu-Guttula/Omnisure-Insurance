# Epic Title: As a policyholder, I want to view my policy history in the account management module so that I can see my past and current policies.

from flask import Flask
from flask_cors import CORS
from backend.routes.policy_history import policy_history_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(policy_history_bp)

if __name__ == '__main__':
    app.run(debug=True)