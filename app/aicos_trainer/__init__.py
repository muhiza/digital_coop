from flask import Blueprint

aicos_trainer = Blueprint('aicos_trainer', __name__, template_folder='templates')

from . import views