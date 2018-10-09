from flask import Blueprint

aicos_mgt = Blueprint('aicos_mgt', __name__,
							template_folder='templates')

from . import views
