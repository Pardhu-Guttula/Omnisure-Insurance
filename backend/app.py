# Epic Title: User Registration using Email and Password

from flask import Flask
from backend.routes.registration import registration_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(registration_bp)

if __name__ == '__main__':
    app.run(debug=True)