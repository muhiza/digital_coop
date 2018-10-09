from flask import Blueprint

aicos_proof = Blueprint('aicos_proof', __name__,
							template_folder='templates')

from . import views
