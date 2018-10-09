from flask import Blueprint

aicos_eregister = Blueprint('aicos_eregister', __name__,
							template_folder='templates')

from . import views
