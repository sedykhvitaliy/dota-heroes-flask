from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()

from app import routes, models
