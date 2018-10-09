from flask import Blueprint

aicos_backup = Blueprint('aicos_backup', __name__,
							template_folder='templates')

from . import views
