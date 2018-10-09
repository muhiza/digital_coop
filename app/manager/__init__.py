from flask import Blueprint

manager = Blueprint('manager', __name__, template_folder="templates")

from .import views