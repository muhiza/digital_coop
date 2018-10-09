from flask import render_template
from .import tumika


























from flask import render_template, abort, flash, redirect, url_for, request
from flask_login import current_user, login_required
from ..models import * 
from .forms import *
import flask_excel
import flask_excel as excel

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

def check_admin():
    #form = LoginForm()
    # departments = Employee.query.filter_by(email=form.email.data).first()
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        #if not current_user.
        abort(403)


def check_overall():
    if not current_user.is_overall:
        abort(403)




def check_coop_admin():
    if not current_user.is_coop_admin:
        abort(403)














@tumika.route('/admin/cooperative/communications')
def messages():
    communications = Communication.query.all()
    return render_template("messages.html", 
        communications=communications, title="List of recent Communication")













@tumika.route('/cooperative/send/message', methods=['GET', 'POST'])
@login_required
def message():
    check_admin()
    form = communicationForm()
    if form.validate_on_submit():
        com = Communication(

                        ms_from=form.ms_from.data,
                        to=form.to.data,
                        message=form.message.data,
                        comment   = form.comment.data,
                        department_id = current_user.email)

        notif = Notification(action="Communication",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            to_number = '+250786012383'
            message = current_user.email + ' Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

            db.session.add(com)
            db.session.add(notif)
            db.session.commit()
            flash("You have successfully send a message")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('tumika.messages'))
    return render_template("message.html", form=form, title="Add Communication")






















@tumika.route('/')
def dashboardw():
	return render_template('dashboardw.html')




"""
@tumika.route('/message')
def message():
	return render_template('message.html', title="Compose and send message")
"""
