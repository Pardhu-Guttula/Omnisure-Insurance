# Epic Title: As an administrator, I want to visualize data using React, so that I can have an interactive and responsive user interface.

from flask import Flask
from flask_cors import CORS
from backend.routes.data import data_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(data_bp)

if __name__ == '__main__':
    app.run(debug=True)