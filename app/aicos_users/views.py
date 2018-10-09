from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from . import aicos_users
from .. import db
from ..models import Employee, Notification, Member

import socket


hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)




#client = nexmo.Client(key='e88f8d53', secret='w7j2m7zksG7RPPVc')


@aicos_users.route('/')
def index():
	return render_template('members_dashboard/index.html')