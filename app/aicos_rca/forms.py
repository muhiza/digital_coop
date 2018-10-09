from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField



class TrainingForm(FlaskForm):
    ingingo = SelectField(
        'Ingingo yaamahugurwa',
        choices=[('Imiyoborere', 'Imiyoborere'), ('Iterambere', 'Iterambere'), ('Umusaruro namasoko', 'Umusaruro namasoko'), ('Ibindi', 'Ibindi')])
    
    trainer = SelectField(
        'Uzatanga Amahugurwa',
        choices=[('RCA', 'RCA'), ('Minicom', 'Minicom'), ('MiTECH', 'MiTECH'), ('Minaloc', 'Minaloc'),
                 ('Rwanda Online', 'Rwanda Online'), ('RURA', 'RURA'), ('JICA', 'JICA'), ('GIZ', 'GIZ'), ('USAID', 'USAID')])

    about = StringField('Ibyerekeye amahugurwa', validators=[DataRequired()], render_kw={"placeholder" : "Andika amazina ibyerekeye y'ingingo y'amahugurwa"})
    description = TextAreaField('Ubusobanuro burambuye', validators=[DataRequired()], render_kw={"placeholder" : "Andika ubusobanuro burambuye ku mahugurwa"})
    date       = DateField('Igihe azatangirwa', validators=[DataRequired()])

    submit      = SubmitField('Ohereza')



class applyTrainingForm(FlaskForm):
    ingingo = SelectField(
        'Ingingo yaamahugurwa',
        choices=[('Imiyoborere', 'Imiyoborere'), ('Iterambere', 'Iterambere'), ('Umusaruro namasoko', 'Umusaruro namasoko'), ('Ibindi', 'Ibindi')])
    abouta = StringField('Ibyerekeye amahugurwa', validators=[DataRequired()], render_kw={"placeholder" : "Andika amazina ibyerekeye y'ingingo y'amahugurwa"})
    descriptiona = TextAreaField('Ubusobanuro burambuye', validators=[DataRequired()], render_kw={"placeholder" : "Andika ubusobanuro burambuye ku mahugurwa"})
    datea       = DateField('Igihe azatangirwa', validators=[DataRequired()])

    submit      = SubmitField('Ohereza')
