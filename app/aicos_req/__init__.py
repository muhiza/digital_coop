from flask import Blueprint


aicos_req = Blueprint('aicos_req', __name__, 
						template_folder='templates')

from . import views