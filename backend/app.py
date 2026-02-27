# Epic Title: Create travel insurance policy schema in PostgreSQL

from flask import Flask
from backend.routes.travel_insurance import travel_insurance_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(travel_insurance_bp)

if __name__ == '__main__':
    app.run(debug=True)