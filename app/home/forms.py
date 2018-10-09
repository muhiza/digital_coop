from flask_wtf import FlaskForm

from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import *
from .. import *

from markupsafe import Markup


class ApplicationForm(FlaskForm):
    Emaila =  StringField("Email yawe", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina ribanza"})
    firstNamea =  StringField("Izina ribanza", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina ribanza"})
    secondNamea =  StringField("Izina rikurikira", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina rikurikira"})
    othersa =  StringField("Ayandi (Singombwa)", render_kw={"placeholder": "Ayandi (Singombwa)"})
    Districta =  StringField("Akarere", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Akarere"})
    Sectora =  StringField("Umurenge", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umurenge"})
    Cella =  StringField("Akagari", validators=[DataRequired()], render_kw={"placeholder": "Injizamo akagari"})
    nIda =  StringField("Nimero ndangamuntu", validators=[DataRequired()], render_kw={"placeholder": "Injiza Nimero y'indangamuntu"})
    entryDatea =  DateField("Tariki yinjiriyemo",format='%Y-%m-%d', validators=[DataRequired()])
    sharea =  StringField("Umugabane", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umugabane"})
    exitDatea =  DateField("Tariki yasohokeyemo",format='%Y-%m-%d', validators=[DataRequired()])
    umuzunguraa =  StringField("Umuzungura", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umuzungura"})
    umukonoa =  StringField("Umukono", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umukono"})
    gendera = SelectField(
        'Igitsina',
        choices=[('Igitsina', 'Igitsina'), ('Gabo', 'Gabo'), ('Gole', 'Gole'), ('Ibindi', 'Ibindi')])
    doba     =  DateField("Tariki y'amavuko", format='%Y-%m-%d', validators=[DataRequired()])  
    phonea = StringField("Nimero ya telephone", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo numero ya telephone"})
    amashuria = SelectField(
        'Amashuri',
        choices=[('Amashuri', 'Amashuri'), ('Abatarize', 'Abatarize'), ('Abanza', 'Abanza'), ('Ayisumbuye', 'Ayisumbuye'), 
                 ('Kaminuza', 'Kaminuza'), ('Imyuga', 'Imyuga')])
    ubumugaa = SelectField(
    'Ubumuga',
    choices=[('Ubumuga', 'Ubumuga'), ('Amaguru', 'Amaguru'), ('Amaboko', 'Amaboko'), ('Kutabona', 'Kutabona'), 
             ('Kutumva', 'Kutumva'), ('Mu mutwe', 'Mu mutwe'), ('Ibindi', 'Ibindi')])

    submit      =  SubmitField('Ohereza')




class ProfileForm(FlaskForm):
    # Education
    primary_school = StringField("Primary School")
    secondary_school = StringField("Secondary School")
    university_school    = StringField("University")
    vocational_school    = StringField("Vocation training center")

    # Experiance.
    exp1 = StringField("Experiance one")
    exp2 = StringField("Experiance two")
    exp3  = StringField("Experiance three")


    # Strength.
    strn1 = StringField("Strength one")
    strn2 = StringField("Strength two")
    strn3 = StringField("Strength three")


    # Careeers.

    car1 = StringField("Career one")
    car2 = StringField("Career two")
    car3 = StringField("Career three")


    # Interests.
    inter1 = StringField("Interest one")
    inter2 = StringField("Interest two")
    inter3 = StringField("Interest three",render_kw={"placeholder": "Your interest: Eg, music, football"})
    # Locations.
    #district = StringField("Location (District)")

    district = SelectField(
        'Programming Language',
        choices=[('kyz', 'Kayonza'), ('kcr', 'Kicukiro'), ('gsb', 'Gasabo'), ('nyg', 'Nyarugenge')]
    )
    submit = SubmitField("Submit")




class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    Code = StringField(u'Code ya Koperative', validators=[DataRequired()], render_kw={"placeholder": "Injiza Code ya Koperative"})
    Name = StringField(u'Izina rya Koperative', validators=[DataRequired()], render_kw={"placeholder": "Injiza izina rya Koperative"})
    RegDate = StringField(u'Igihe Koperative yandikiwe', validators=[DataRequired()], render_kw={"placeholder": "Injiza italiki yandikiweho"})
    Certificate = StringField(u'Certificate ya Koperative', validators=[DataRequired()], render_kw={"placeholder": "Shyiramo certificate ya Koperative"})
    Province = SelectField(
        'Intara Koperative ibarizwamo',
        choices=[('Intara', 'Intara'),('Kigali City', 'Kigali City'), 
        ('East', 'East'), ('West', 'West'),
        ('North', 'North'), ('South', 'South')])

    District = SelectField(
        'Akarere Koperative ibarizwamo',
        choices=[('Akarere', 'Akarere'),('Nyarugenge', 'Nyarugenge'), 
        ('Gasabo', 'Gasabo'), ('Kicukiro', 'Kicukiro'),
        ('Kayonza', 'Kayonza'), ('Kirehe', 'Kirehe'),
        ('Ngoma', 'Ngoma'), ('Bugesera', 'Bugesera'),
        ('Nyagatare', 'Nyagatare'), ('Gatsibo', 'Gatsibo'),


        ('Kamonyi', 'Kamonyi'), ('Ruhango', 'Ruhango'),
        ('Muhanga', 'Muhanga'), ('Nyanza', 'Nyanza'),
        ('Huye', 'Huye'), ('Nyaruguru', 'Nyaruguru'),

        ('Rulindo', 'Rulindo'), ('Burera', 'Burera'),
        ('Gakenke', 'Gakenke'), ('Gicumbi', 'Gicumbi'),
        ('Musanze', 'Musanze'),


        ('Karongi', 'Karongi'), ('Ngororero', 'Ngororero'),
        ('Nyabihu', 'Nyabihu'), ('Nyamasheke', 'Nyamasheke'),

        ('Rubavu', 'Rubavu'), ('Rusizi', 'Rusizi'),
        ('Rutsiro', 'Rutsiro')])
    Sector = StringField('Injiza umurenge Koperative ibarizwamo', validators=[DataRequired()], render_kw={"placeholder": "Injiza umurenge Koperative ibarizwamo"})
    Cell = StringField('Injiza akagari Koperative ibarizwamo', validators=[DataRequired()], render_kw={"placeholder": "Injiza akagari Koperative ibarizwamo"})
    startingShare = StringField('Umugabane Shingiro', validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wo Kwinjira muri Cooperative"})
    Field = SelectField(
        'Hitamo umurimo Koperative ikora',
        choices=[('Umurimo Koperative ikora', 'Umurimo Koperative ikora'),('Ubuhinzi bw\'Icyayi', 'Ubuhinzi bw\'Icyayi'), 
        ('Ubucukuzi', 'Ubucukuzi'), ('Ubworozi', 'Ubworozi'),
        ('Ubuhinzi bwa Kawa', 'Ubuhinzi bwa Kawa'), ('Ubuhinzi bw\'Imyumbati', 'Ubuhinzi bw\'Imyumbati'),
        ('Ubuhinzi bw\'Ibirayi', 'Ubuhinzi bw\'Ibirayi'), ('Gutwara moto', 'Gutwara Moto'),
        ('Ubuvumvu', 'Ubuvumvu'), ('Ubuhinzi bw\'Ibireti', 'Ubuhinzi bw\'Ibireti'),
        ('Ubuhinzi bw\'Umuceri', 'Ubuhinzi bw\'Umuceri'), ('Gutwara imodoka', 'Gutwara imodoka'),
        ('Ubuhinzi bw\'Ibigori', 'Ubuhinzi bw\'Ibigori'), ('Uburobyi', 'Uburobyi'),
        ('Ubuhinzi bw\'Indabo', 'Ubuhinzi bw\'Indabo'), ('Kuboha', 'Kuboha')])



    Federation = SelectField(
        'Hitamo Federasiyo ya Koperative',
        choices=[('Federasiyo ya Koperative', 'Federasiyo ya Koperative'), 
        ('FERWACOTAMO', 'FERWACOTAMO'), ('FERWACAPI', 'FERWACAPI'),
        ('FUCORIRWA', 'FUCORIRWA'), ('RFTC', 'RFTC'),
        ('FERWACOTHE', 'FERWACOTHE'), ('FCMR', 'FCMR'),
        ('RFWC', 'RFWC'), ('FECOPPORWA', 'FECOPPORWA'),
        ('RWCCF', 'RWCCF'), ('RCCF', 'RCCF'),
        ('NDFFR', 'NDFFR'), ('RFHC', 'RFHC'),
        ('FEFICOORWA', 'FEFICOORWA')])


    Union = SelectField(
        'Hitamo Union Koperative ibarizwamo',
        choices=[('Hitamo Union Koperative ibarizwamo', 'Hitamo Union Koperative ibarizwamo'),('UCTHEN', 'UCTHEN'), 
        ('UCTCCN', 'UCTCCN'), ('UCOTHENYU', 'UCOTHENYU'),
        ('UCOTHEI', 'UCOTHEI'), ('UCOTHESN', 'UCOTHESN')])


    Description = TextAreaField('Ubundi busobanuro bwa Koperative (Si ngombwa)', render_kw={"placeholder": "Ubundi busobanuro bwa Koperative (Si ngombwa)"})

    submit = SubmitField('Injiza muri sisiteme')














class newDepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    Name = StringField(Markup('<b>Izina rya Koperative</b>'), validators=[DataRequired()], render_kw={"placeholder": "Injiza izina rya Koperative"})
    Province = SelectField(
        Markup('<b>Intara Koperative ibarizwamo</b>'),
        choices=[('Intara', 'Intara'),('Kigali City', 'Kigali City'), 
        ('East', 'East'), ('West', 'West'),
        ('North', 'North'), ('South', 'South')])

    District = SelectField(
        Markup('<b>Akarere Koperative ibarizwamo</b>'),
        choices=[('Akarere', 'Akarere'),('Nyarugenge', 'Nyarugenge'), 
        ('Gasabo', 'Gasabo'), ('Kicukiro', 'Kicukiro'),
        ('Kayonza', 'Kayonza'), ('Kirehe', 'Kirehe'),
        ('Ngoma', 'Ngoma'), ('Bugesera', 'Bugesera'),
        ('Nyagatare', 'Nyagatare'), ('Gatsibo', 'Gatsibo'),


        ('Kamonyi', 'Kamonyi'), ('Ruhango', 'Ruhango'),
        ('Muhanga', 'Muhanga'), ('Nyanza', 'Nyanza'),
        ('Huye', 'Huye'), ('Nyaruguru', 'Nyaruguru'),

        ('Rulindo', 'Rulindo'), ('Burera', 'Burera'),
        ('Gakenke', 'Gakenke'), ('Gicumbi', 'Gicumbi'),
        ('Musanze', 'Musanze'),


        ('Karongi', 'Karongi'), ('Ngororero', 'Ngororero'),
        ('Nyabihu', 'Nyabihu'), ('Nyamasheke', 'Nyamasheke'),

        ('Rubavu', 'Rubavu'), ('Rusizi', 'Rusizi'),
        ('Rutsiro', 'Rutsiro')])
    Sector = StringField(Markup('<b>Injiza umurenge Koperative ibarizwamo</b>'), validators=[DataRequired()], render_kw={"placeholder": "Injiza umurenge Koperative ibarizwamo"})
    Cell = StringField(Markup('<b>Injiza akagari Koperative ibarizwamo</b>'), validators=[DataRequired()], render_kw={"placeholder": "Injiza akagari Koperative ibarizwamo"})
    startingSharex = StringField(Markup('<b>Umugabane Shingiro</b>'), validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wo Kwinjira muri Cooperative"})
    sharePerPerson = StringField(Markup('<b>Umugabane Kuri buri munyamuryango</b>'), validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wo Kwinjira muri Cooperative"})
    maleMembers = StringField(Markup('<b>Abanyamuryango b\'abagabo</b>'), validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wo Kwinjira muri Cooperative"})
    femaleMembers = StringField(Markup('<b>Abanyamuryango b\'abagore</b>'), validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wo Kwinjira muri Cooperative"})

    submit = SubmitField('Injiza muri sisiteme')
