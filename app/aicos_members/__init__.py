from flask import Blueprint


aicos_members = Blueprint('aicos_members', __name__, 
						template_folder='templates')

from . import views