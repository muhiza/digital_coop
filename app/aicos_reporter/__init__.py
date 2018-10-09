from flask import Blueprint

aicos_reporter = Blueprint('aicos_reporter', __name__,
							template_folder='templates')

from . import views
