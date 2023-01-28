from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bootstrap = Bootstrap4(app)

with app.app_context():
    db.create_all()

from app import routes, models
