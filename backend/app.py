# Epic Title: As a user, I want to enable two-factor authentication, so that I can secure my account with an additional layer of protection.

from flask import Flask
from flask_cors import CORS
from backend.routes.auth import auth_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)