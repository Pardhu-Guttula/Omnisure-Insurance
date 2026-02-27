# Epic Title: As an insurer, I want to view interactive dashboards, so that I can get a quick overview of key metrics and actionable insights.

from flask import Flask
from flask_cors import CORS
from backend.routes.dashboard import dashboard_bp
from backend.routes.metric import metric_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(metric_bp)

if __name__ == '__main__':
    app.run(debug=True)