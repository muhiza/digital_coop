from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField



class TrainingForm(FlaskForm):
    name  = StringField('Izina ryamahugurwa', validators=[DataRequired()], render_kw={"placeholder" : "Andika amazina y'ingingo y'amahugurwa"})
    about = StringField('Ibyerekeye amahugurwa', validators=[DataRequired()], render_kw={"placeholder" : "Andika amazina ibyerekeye y'ingingo y'amahugurwa"})
    description = TextAreaField('Ubusobanuro burambuye', validators=[DataRequired()], render_kw={"placeholder" : "Andika ubusobanuro burambuye ku mahugurwa"})
    date        = DateField('Igihe azatangirwa', validators=[DataRequired()])

    submit      = SubmitField('Ohereza')





class applyTrainingForm(FlaskForm):
    ingingo = SelectField(
        'Ingingo yaamahugurwa',
        choices=[('Imiyoborere', 'Imiyoborere'), ('Iterambere', 'Iterambere'), ('Umusaruro namasoko', 'Umusaruro namasoko'), ('Ibindi', 'Ibindi')])
    abouta = StringField('Ibyerekeye amahugurwa', validators=[DataRequired()], render_kw={"placeholder" : "Andika amazina ibyerekeye y'ingingo y'amahugurwa"})
    descriptiona = TextAreaField('Ubusobanuro burambuye', validators=[DataRequired()], render_kw={"placeholder" : "Andika ubusobanuro burambuye ku mahugurwa"})
    datea       = DateField('Igihe azatangirwa', validators=[DataRequired()])

    submit      = SubmitField('Ohereza')
