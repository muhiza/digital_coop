from flask import Blueprint

aicos_users = Blueprint('aicos_users', __name__, template_folder="templates", static_folder="static");

from . import views