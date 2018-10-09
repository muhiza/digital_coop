from flask import Blueprint

aicos_imboni = Blueprint('aicos_imboni', __name__,
							template_folder='templates')

from . import views
