from flask import Flask
from flask_cors import CORS
from censo_service import censo

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(censo, url_prefix='/api/censo')

@app.route('/')
def hello():
    return "API de censo"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

