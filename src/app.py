from flask import Flask
from flask_login import LoginManager

from database import db
from config import DATABASE_URL, APP_KEY


app = Flask(__name__)
app.config["SECRET_KEY"] = APP_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()
