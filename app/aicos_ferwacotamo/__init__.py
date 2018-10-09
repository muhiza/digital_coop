from flask import Blueprint

aicos_ferwacotamo = Blueprint('aicos_ferwacotamo', __name__, template_folder='templates')

from . import views