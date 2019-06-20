from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# from app.config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    # app.config.from_object(DevelopmentConfig)
    return app

app = create_app()
db = SQLAlchemy(app)
db.init_app(app)
CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(app)
