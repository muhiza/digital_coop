from flask import Blueprint

aicos_confederation = Blueprint('aicos_confederation', __name__, template_folder='templates')

from . import views