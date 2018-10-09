from flask import Blueprint

aicos_pm = Blueprint('aicos_pm', __name__,
							template_folder='templates')

from . import views
