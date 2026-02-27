# Epic Title: As a frontend developer, I want to implement performance optimization techniques for the React frontend, so that it loads faster and provides a smooth user experience.

from flask import Flask
from flask_cors import CORS
from backend.routes.asset import asset_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(asset_bp)

if __name__ == '__main__':
    app.run(debug=True)