# Epic Title: OAuth Integration for Social Logins

from flask import Flask
from backend.routes.oauth import oauth_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(oauth_bp)

if __name__ == '__main__':
    app.run(debug=True)