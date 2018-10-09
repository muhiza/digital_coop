from flask import Blueprint

aicos_stock_managment = Blueprint('aicos_stock_managment', __name__, template_folder="templates")

from . import views