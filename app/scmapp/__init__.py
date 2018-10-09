from flask import Blueprint

supply_chain = Blueprint('supply_chain', __name__, template_folder="templates")

from . import views
