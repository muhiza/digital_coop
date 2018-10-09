from flask import Flask, Blueprint

aicos_wcm = Blueprint('aicos_wcm', __name__, template_folder="templates")

from .views import *