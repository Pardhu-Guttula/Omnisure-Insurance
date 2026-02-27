# Epic Title: Create life insurance policy schema in PostgreSQL

from flask import Flask
from backend.routes.life_insurance import life_insurance_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(life_insurance_bp)

if __name__ == '__main__':
    app.run(debug=True)