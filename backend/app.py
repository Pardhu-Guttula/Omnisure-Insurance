# Epic Title: As a user, I want to adhere to secure password policies, so that I can enhance the security of my account.

from flask import Flask
from flask_cors import CORS
from backend.routes.security import security_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(security_bp)

if __name__ == '__main__':
    app.run(debug=True)