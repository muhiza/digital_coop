from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email


#from ..models import Department, Role, Employee, Product
from ..models import *


from flask_wtf.file import FileField, FileAllowed, FileRequired
from .. import images



class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Amazina', validators=[DataRequired()])
    description = TextAreaField('Ubusobanuro', validators=[DataRequired()])
    submit = SubmitField('Injiza')


class StaffForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Second Name', validators=[DataRequired()])
    Nid = StringField('Nid', validators=[DataRequired()])
    District = StringField('District', validators=[DataRequired()])
    Sector = StringField('Sector', validators=[DataRequired()])
    Sex = StringField('Sex', validators=[DataRequired()])
   
    Yob = StringField('Year of birth', validators=[DataRequired()])
    Position = StringField('Position', validators=[DataRequired()])
    Education = StringField('Education', validators=[DataRequired()])
    
    Telephone = StringField('Telephone', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired()])
    monthlyNetSalary = StringField('Monthly net salary', validators=[DataRequired()])
    submit = SubmitField('Submit')



class ActivityForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Activity Name', validators=[DataRequired()])
    description = TextAreaField('Activity Description', validators=[DataRequired()])
    submit = SubmitField('Submit')



class AssetForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    assetType = SelectField(
        'Ubwoko bw\'umutungo',
        choices=[('Ikibanza', 'Ikibanza'), ('Ishyamba', 'Ishyamba'), ('Inzu', 'Inzu'), 
                ('Amatungo', 'Amatungo'), ('Imodoka', 'Imodoka')])

    assetLocation = SelectField(
        'Aho umutungo uherereye',
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

    assetValue = StringField('Agaciro kawo', validators=[DataRequired()])
    description = TextAreaField('Ibindi bisobanuro', validators=[DataRequired()])
    submit = SubmitField('Injiza')





class ReportForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    status = SelectField(
        'Status',
        choices=[('Uko bihagaze', 'Uko bihagaze'), ('Byararangiye', 'Byararangiye'), ('Biracyakomeje', 'Biracyakomeje'), 
                ('Ntibiratangira gukorwaho', 'Ntibiratangira gukorwaho')])
    project = StringField('Izina ry umushinga', validators=[DataRequired()], render_kw={"placeholder": "Andika Izina ry'umushinga"})
    task = StringField('Izina ry igikorwa', validators=[DataRequired()], render_kw={"placeholder": "Andika izina ry'igikorwa"})
    description = TextAreaField('Ubusobanuro', validators=[DataRequired()], render_kw={"placeholder": "Andika Ubusobanuro"})
    notes = TextAreaField('Andika ibindi (Ntago ari ngombwa)', validators=[DataRequired()], render_kw={"placeholder": "Andika ibindi (Ntago ari ngombwa)"})
    submit = SubmitField('Ohereza')






class DecForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    status = SelectField(
        'Status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    decision =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner = QuerySelectField(query_factory=lambda: Employee.query.filter_by(first_name=current_user.first_name), get_label="first_name")
    stakeholders = StringField("Stakeholders", validators=[DataRequired()])
    due_date    =  DateField("Due date",format='%Y-%m-%d', validators=[DataRequired()])
    background  =  StringField("Background", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])

    submit      =  SubmitField('Create')



class MemberForm(FlaskForm):
    izina_ribanzax =  StringField("Izina ribanza", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina ribanza", "id": "izina_ribanza"})
    izina_rikurikirax =  StringField("Izina rikurikira", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina rikurikira", "id": "izina_rikurikira"})
    ayandix =  StringField("Ayandi (Singombwa)", render_kw={"placeholder": "Ayandi (Singombwa)", "id": "ayandi"})
    igitsinax =  SelectField(
        'Igitsina',
        choices=[('Igitsina', 'Igitsina'), ('Gabo', 'Gabo'), ('Gore', 'Gore')])
    indangamuntux =  IntegerField("Indangamuntu", validators=[DataRequired()], render_kw={"placeholder": "Injiza nomero y'indangamuntu", "id": "indangamuntu"})
    codex =  StringField("Code", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo code y'umunyamuryango", "id": "code"})
    
    tariki_yavukiyex =  DateField("Tariki y'amavuko", format='%Y-%m-%d', validators=[DataRequired()])
    intarax =  StringField("Intara", validators=[DataRequired()], render_kw={"placeholder": "Injiza intara", "id": "intara"})
    akarerex =  StringField("Akarere", validators=[DataRequired()], render_kw={"placeholder": "Injiza akarere"})
    umurengex =  StringField("Umurenge", validators=[DataRequired()], render_kw={"placeholder": "Injiza umurenge"})
    akagarix =  StringField("Akagari", validators=[DataRequired()], render_kw={"placeholder": "Injiza akagari"})
    
    umudugudux =  StringField("Umudugudu", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umudugudu", "id": "umudugudu"})
    tariki_yinjiriyex =  DateField("Taliki y'injiriye", format='%Y-%m-%d', validators=[DataRequired()])
    umugabanex = StringField("Umugabane", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umugabane w'umunyamuryango", "id": "umugabane"})
    umukonox     =  StringField("Umukono", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umukono w'umunyamuryango", "id": "umukono"})  
    nomero_ya_telephonex = StringField("Nimero ya telephone", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo numero ya telephone", "id": "nomero_ya_telephone"})
    
    amashurix = SelectField(
        'Amashuri',
        choices=[('Amashuri', 'Amashuri'), ('Abatarize', 'Abatarize'), ('Abanza', 'Abanza'), ('Ayisumbuye', 'Ayisumbuye'), 
                 ('Kaminuza', 'Kaminuza'), ('Imyuga', 'Imyuga')])
    ubumugax = SelectField(
    'Ubumuga',
    choices=[('Ubumuga', 'Ubumuga'), ('Amaguru', 'Amaguru'), ('Amaboko', 'Amaboko'), ('Kutabona', 'Kutabona'), 
             ('Kutumva', 'Kutumva'), ('Mu mutwe', 'Mu mutwe'), ('Ibindi', 'Ibindi')])
    arubatsex = SelectField(
    'Arubatse?',
    choices=[('Arubatse', 'Arubatse'), ('Yego', 'Yego'), ('Oya', 'Oya')])
    umubare_wabanax = IntegerField("Umubare w'abana", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Umubare w'abana"})
    icyiciro_cyubudehex = StringField("Icyiciro cy'ubudehe", validators=[DataRequired()], render_kw={"placeholder": "Icyiciro cy'ubudehe"})
    ubwishingizix = StringField("Ubwishingizi", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo ubwishingizi bw'umunyamuryango"})    
    akazi_akora_muri_koperativex = StringField("Akazi Akora Muri Koperative", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo akazi umunyamuryango akora muri Koperative"})
    akandi_kazi_akorax = StringField("Akandi kazi akora", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Akandi kazi akora"})
    ubuso_ahingahox  = StringField("Ubuso ahingaho icyayi", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubuso ahingaho icyayi"})
    
    ubwoko_bwigihingwax = StringField("Ubwoko bw'igihingwa (Icyayi)", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubwoko bw'igihingwa (Cy'icyayi)"})
    ubuso_ahingaho_ibindix  = StringField("Ubuso ahingaho ibindi", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubuso ahingaho ibindi"})
    ubwoko_bwigihingwa_kindix = StringField("Ubwoko bw'ikindi gihingwa", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubwoko bw'ikindi gihingwa ahinga"})
    ubuso_budakoreshwax  = StringField("Ubuso budakoreshwa", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo Ubuso bundi budakoreshwa"})
    


    """
    Current Comment
    ==========================
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    """ 
    
    submit      =  SubmitField('Injiza Umunyamuryango')



class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    cooperative = QuerySelectField(query_factory=lambda: Department.query.filter_by(email='justin@gmail.com'),
                                  get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.filter_by(name='President'),
                            get_label="name")
    submit = SubmitField('Submit')





class PaymentForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    reason = SelectField(
        'Status',
        choices=[('Reason', 'none'), ('Umusanzu', 'Umusanzu'), ('Umugabane', 'Umugabane'),
        ('Amande', 'Amande')])
    amount =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    date    =  DateField("Due date", format='%Y-%m-%d', validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Save')


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





class GoalForm(FlaskForm):

    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])

    name =  StringField("Izina ry'igikorwa", validators=[DataRequired()], render_kw={"placeholder": "Andika izina ry'igikorwa"})
    description =  TextAreaField("Ubusobanuro", validators=[DataRequired()], render_kw={"placeholder": "Andika ubusobanuro bw'igikorwa"})
    amount =  StringField("Amafaranga agomba gutangwa", validators=[DataRequired()], render_kw={"placeholder": "Andika amafaranga akenewe"})
    startingDate     =  DateField("Tariki igikorwa gitangiriye", format='%Y-%m-%d', validators=[DataRequired()],)  
    endingDate     =  DateField("Tariki igikorwa kizarangirira", format='%Y-%m-%d', validators=[DataRequired()])  

    submit      =  SubmitField('Emeza')






