# Epic Title: Store User Credentials Securely in PostgreSQL

from flask import Flask
from backend.routes.user_management import user_management_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(user_management_bp)

if __name__ == '__main__':
    app.run(debug=True)