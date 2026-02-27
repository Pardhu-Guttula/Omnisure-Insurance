# Epic Title: User Login using Email and Password

from flask import Flask
from backend.routes.login import login_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)