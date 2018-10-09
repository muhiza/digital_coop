from flask import Flask, Blueprint

tumika = Blueprint("tumika", __name__, template_folder="templates")

from . import views