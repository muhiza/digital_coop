from flask import render_template
from . import aicos_ezigama

@aicos_ezigama.route('/')
def home():
	return render_template("indexez.html")