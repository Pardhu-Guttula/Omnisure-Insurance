# Epic Title: As a policyholder, I want to track my claims in the account management module so that I can see the status and details of my claims.

from flask import Flask
from flask_cors import CORS
from backend.routes.claim import claim_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(claim_bp)

if __name__ == '__main__':
    app.run(debug=True)