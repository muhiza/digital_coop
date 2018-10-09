from flask import Blueprint


aicos_stock = Blueprint('aicos_stock', __name__, template_folder='templates')

from . import views