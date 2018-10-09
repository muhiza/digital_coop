from flask import Blueprint

aicos_monitor = Blueprint('aicos_monitor', __name__,
							template_folder='templates')

from . import views
