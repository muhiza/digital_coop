from flask import render_template
from . import aicos_imboni

@aicos_imboni.route('/')
def home():
	return render_template("index.html")