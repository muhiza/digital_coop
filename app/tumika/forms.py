from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email

#from ..models import Department, Role, Employee, Product
from ..models import *

from markupsafe import Markup

from flask_wtf.file import FileField, FileAllowed, FileRequired
from .. import images








class communicationForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    ms_from = StringField("Message From", validators=[DataRequired()], render_kw={"placeholder": "Enter Subject"})
    to = SelectField(
        'Message To',
        choices=[('All members', 'All members'), ('All female member', 'All female member'),
         ('All male member', 'All male member'), ('Non members', 'Non members')])
    message =  TextAreaField("Message", validators=[DataRequired()], render_kw={"placeholder": "Enter Message content"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    comment = TextAreaField("Comment", validators=[DataRequired()], render_kw={"placeholder": "Enter Comment (Optional)"})
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Send')

