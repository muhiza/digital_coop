from flask import Blueprint

aicos_stack = Blueprint('aicos_stack', __name__,
							template_folder='templates')

from . import views
