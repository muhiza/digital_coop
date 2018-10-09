from flask import Blueprint


aicos_acc = Blueprint('aicos_acc', __name__, 
						template_folder='templates')

from . import views