from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email

#from ..models import Department, Role, Employee, Product
from ..models import *


from flask_wtf.file import FileField, FileAllowed, FileRequired
from .. import images






class intekoRusangeForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    ibyizweho = SelectField(
        'Status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    decision1 =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner1 = StringField("Ibyemezo", validators=[DataRequired()])
    stakeholders1 = StringField("Abitabiriye Inama", validators=[DataRequired()])
    due_date1    =  DateField("Talika",format='%Y-%m-%d', validators=[DataRequired()])
    background1  =  StringField("Ubusobanuro burambuye", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])

    submit      =  SubmitField('Emeza')


