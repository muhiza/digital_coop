from flask import render_template
from . import aicos_pm

@aicos_pm.route('/')
def aicos_pm_home():
	return render_template("indexzx.html")

