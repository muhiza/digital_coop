from flask import Blueprint

aicos_cb = Blueprint('aicos_cb', __name__,
							template_folder='templates')

from . import views
