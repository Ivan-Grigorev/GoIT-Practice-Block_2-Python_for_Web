from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from noteapp.auth import routes
