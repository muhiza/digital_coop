from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_stock
from flask_login import current_user, login_required
from ..models import * 
from .forms import *

import flask_excel
import flask_excel as excel

import nexmo

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)





client = nexmo.Client(key='e7096025', secret='ab848459dae27b51')



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

@aicos_stock.route('/')
def dashboardqw():
    return render_template('index.html')


