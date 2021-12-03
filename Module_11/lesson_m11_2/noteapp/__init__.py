from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from noteapp.config import Config
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
mail = Mail(app)




from noteapp.models import User, Note
from noteapp.auth.routes import auth_bp
from noteapp.notes.routes import note_bp

app.register_blueprint(auth_bp)
app.register_blueprint(note_bp)
