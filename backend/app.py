# Epic Title: As a system architect, I want to implement caching strategies in both frontend and backend, so that the system can handle a larger number of requests efficiently.

from flask import Flask
from flask_cors import CORS
from backend.routes.cache import cache_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(cache_bp)

if __name__ == '__main__':
    app.run(debug=True)