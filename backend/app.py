# Epic Title: As a data engineer, I want data encryption in the PostgreSQL database, so that sensitive data is protected at rest.

from flask import Flask
from flask_cors import CORS
from backend.routes.encryption import encryption_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(encryption_bp)

if __name__ == '__main__':
    app.run(debug=True)