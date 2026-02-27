# Epic Title: As a system administrator, I want to implement load balancing strategies, so that the server load is distributed evenly and system availability is improved.

from flask import Flask
from flask_cors import CORS
from backend.routes.load_balancer import load_balancer_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(load_balancer_bp)

if __name__ == '__main__':
    app.run(debug=True)