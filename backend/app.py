# Epic Title: As a developer, I want to implement the agent onboarding UI using React, so that insurance agents have an intuitive interface to register and onboard.

from flask import Flask
from flask_cors import CORS
from backend.routes.registration import registration_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(registration_bp)

if __name__ == '__main__':
    app.run(debug=True)