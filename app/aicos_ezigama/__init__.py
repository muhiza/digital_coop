from flask import Blueprint

aicos_ezigama = Blueprint('aicos_ezigama', __name__,
							template_folder='templates', static_folder="static")

from . import views
