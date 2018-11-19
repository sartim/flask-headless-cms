import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from skeleton.app.config import DevelopmentConfig, ProductionConfig, TestingConfig


dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', '.env'))
load_dotenv(dotenv_path)


def create_app():
    app = Flask(__name__)

    if os.environ.get('DEV') == "TRUE":
        app.config.from_object(DevelopmentConfig)

    if os.environ.get('PROD') == "TRUE":
        app.config.from_object(ProductionConfig)

    if os.environ.get("TEST") == "TRUE":
        app.config.from_object(TestingConfig)

    return app


# Run create_app on init
app = create_app()

db = SQLAlchemy(app)
db.init_app(app)

CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)

if __name__ == "__main__":
    app.run(app)
