from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, email


class userInfoForm(FlaskForm):
	firstname = StringField('First Name', validators=[DataRequired()])
	secondname = StringField('Second Name', validators=[DataRequired()])
	submit 	   = SubmitField('Submit')