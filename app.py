from flask import Flask
from config import Config
from models import db
from routes import routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(routes)

@app.route("/")
def home():
    return "Job Tracker API is running"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(debug=True)