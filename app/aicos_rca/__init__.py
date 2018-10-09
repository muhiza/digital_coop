from flask import Blueprint

aicos_rca = Blueprint('aicos_rca', __name__, template_folder='templates')

from . import views