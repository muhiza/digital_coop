from flask import Blueprint

aicos_union = Blueprint('aicos_union', __name__, template_folder='templates')

from . import views