from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, StringField, SubmitField, SelectField,  ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('', validators=[DataRequired(), Email()], render_kw={"placeholder": "Kode yo kwinjira (Email)"})
    username = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Izina ukoresha"})
    first_name = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Izina ribanza"})
    last_name = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Izina rikurikira"})
    phone_number = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Nomero ya telephone igendanwa"})
    password = PasswordField('', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ], render_kw={"placeholder": "Ijambo ry\'Ibanga"})
    confirm_password = PasswordField('', render_kw={"placeholder": "Ongera wandike ijambo ry\'Ibanga"})


    #recaptcha = RecaptchaField()


    submit = SubmitField('OHEREZA')

    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('', validators=[DataRequired(), Email()], render_kw={"placeholder": "Kode yo kwinjira (Email)"})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Ijambo ry'ibinga"})
    #recaptcha = RecaptchaField()
    submit = SubmitField('KWINJIRA', render_kw={"onclick": "loading()"})


class ForgetPasswordForm(FlaskForm):
    """
    Form for user to change password
    """
    email = StringField('', validators=[DataRequired(), Email()], render_kw={"placeholder": "Kode yo kwinjira"})

    submit = SubmitField('Ohereza')
