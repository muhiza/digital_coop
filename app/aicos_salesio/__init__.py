from flask import Blueprint

aicos_salesio = Blueprint('aicos_salesio', __name__,
							template_folder='templates')

from . import views
