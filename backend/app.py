# Epic Title: As a database administrator, I want to optimize MySQL database queries and implement proper indexing, so that the overall database performance is improved.

from flask import Flask
from flask_cors import CORS
from backend.routes.query import query_bp
from backend.routes.index import index_bp

app = Flask(__name__)
CORS(app)  # To enable CORS

# Register blueprints
app.register_blueprint(query_bp)
app.register_blueprint(index_bp)

if __name__ == '__main__':
    app.run(debug=True)