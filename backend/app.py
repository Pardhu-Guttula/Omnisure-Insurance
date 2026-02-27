# Epic Title: Password Management

from flask import Flask
from backend.routes.password_reset import password_reset_bp
from backend.routes.change_password import change_password_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(password_reset_bp)
app.register_blueprint(change_password_bp)

if __name__ == '__main__':
    app.run(debug=True)