from flask import Blueprint

aicos_finance = Blueprint('aicos_finance', __name__,
							template_folder='templates')

from . import views
