# Epic Title: As a mobile user, I want mobile-specific optimizations, so that I can make use of enhanced mobile functionalities.

from flask import Flask
from flask_cors import CORS
from backend.routes.mobile import mobile_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(mobile_bp)

if __name__ == '__main__':
    app.run(debug=True)