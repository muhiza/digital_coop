from flask import  render_template
from . import aicos_cb


@aicos_cb.route('/')
def home():
	return render_template('muhiza.html')
	
@aicos_cb.route('/show_details')
def showDetails():
	return render_template('show.html')

@aicos_cb.route('/add_new_content')
def addNewContent():
	return render_template('add_new.html')
	


