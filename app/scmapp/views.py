from flask import render_template
#from models import *

from . import supply_chain
@supply_chain.route('/')
def dashboardzxc():
	return render_template("dashboard.html")


