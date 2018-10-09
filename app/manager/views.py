from flask import render_template, url_for, flash, redirect
from . import manager
from .forms import *
from ..models import *



@manager.route('/')
def managerIndex():
	return render_template("manageHome.html")


@manager.route('/userInfo', methods=['POST', 'GET'])
def userInfoNew():

	form = userInfoForm()
	if form.validate_on_submit():
		newInfo = userInfo(
					firstname = form.firstname.data,
					secondname = form.secondname.data
					)
		try:
			db.session.add(newInfo)
			db.session.commit()
			
			flash("Information has been submitted well!")
			return redirect(url_for('manager.managerIndex'))
		except:
			flash("There is an error in the form!")
	return render_template('managerIndex.html', form=form)


