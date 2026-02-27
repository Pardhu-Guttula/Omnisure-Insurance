# Epic Title: As a policyholder, I want secure profile management features in the account management module so that I can update my personal and policy details securely.

from flask import Flask
from flask_cors import CORS
from backend.routes.profile import profile_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(profile_bp)

if __name__ == '__main__':
    app.run(debug=True)