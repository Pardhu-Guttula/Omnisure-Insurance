# Epic Title: As a mobile user, I want the UI to be responsive and mobile-friendly, so that I can access all features comfortably on various mobile devices.

from flask import Flask
from flask_cors import CORS
from backend.routes.user import user_bp
from backend.routes.ui_settings import ui_settings_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(ui_settings_bp)

if __name__ == '__main__':
    app.run(debug=True)