# Epic Title: Create motor insurance policy schema in PostgreSQL

from flask import Flask
from backend.routes.motor_insurance import motor_insurance_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(motor_insurance_bp)

if __name__ == '__main__':
    app.run(debug=True)