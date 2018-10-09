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




class inamaUbuyoboziForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    status = SelectField(
        'Status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    decision =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner = decision =  StringField("Decision", validators=[DataRequired()])
    stakeholders = StringField("Stakeholders", validators=[DataRequired()])
    due_date    =  DateField("Due date",format='%Y-%m-%d', validators=[DataRequired()])
    background  =  StringField("Background", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])

    submit      =  SubmitField('Emeza')





class ubugenzuziForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    status = SelectField(
        'Status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    decision =  StringField("Decision", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner = StringField("Decision", validators=[DataRequired()])
    stakeholders = StringField("Stakeholders", validators=[DataRequired()])
    due_date    =  DateField("Due date",format='%Y-%m-%d', validators=[DataRequired()])
    background  =  StringField("Background", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])

    submit      =  SubmitField('Emeza')







class isandukuForm(FlaskForm):
    
    no =  StringField("Nimero y'igikorwa", validators=[DataRequired()])
    done_date = DateField("Tariki byakoreweho",format='%Y-%m-%d', validators=[DataRequired()])
    action    =  StringField("Igikorwa", validators=[DataRequired()])
    income  =  StringField("Amafaranga yinjiye", validators=[DataRequired()])
    expense  =  StringField("Amafaranga Asohotse", validators=[DataRequired()])
    remain  =  StringField("Amafaranga Asigaye", validators=[DataRequired()])
    done_by  =  StringField("Umukono / Uyatanze ", validators=[DataRequired()])
    done_to  =  StringField("Umukono / Uyakiriye", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Emeza')





class MemberForm(FlaskForm):
    firstName =  StringField("Izina ribanza", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina ribanza"})
    secondName =  StringField("Izina rikurikira", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Izina rikurikira"})
    others =  StringField("Ayandi (Singombwa)", render_kw={"placeholder": "Ayandi (Singombwa)"})
    District =  StringField("Akarere", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Akarere"})
    Sector =  StringField("Umurenge", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umurenge"})
    Cell =  StringField("Akagari", validators=[DataRequired()], render_kw={"placeholder": "Injizamo akagari"})
    nId =  StringField("Nimero ndangamuntu", validators=[DataRequired()], render_kw={"placeholder": "Injiza Nimero y'indangamuntu"})
    entryDate =  DateField("Tariki yinjiriyemo",format='%Y-%m-%d', validators=[DataRequired()])
    share =  StringField("Umugabane", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umugabane"})
    exitDate =  DateField("Tariki yasohokeyemo",format='%Y-%m-%d', validators=[DataRequired()])
    umuzungura =  StringField("Umuzungura", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umuzungura"})
    umukono =  StringField("Umukono", validators=[DataRequired()], render_kw={"placeholder": "Injizamo Umukono"})
    gender = SelectField(
        'Igitsina',
        choices=[('Igitsina', 'Igitsina'), ('Gabo', 'Gabo'), ('Gole', 'Gole'), ('Ibindi', 'Ibindi')])
    dob     =  DateField("Tariki y'amavuko", format='%Y-%m-%d', validators=[DataRequired()])  
    phone = StringField("Nimero ya telephone", validators=[DataRequired()], render_kw={"placeholder": "Shyiramo numero ya telephone"})
    
    
    """
    Current Comment
    ==========================
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    """
    submit      =  SubmitField('Injiza Umunyamuryango')




class umusaruroForm(FlaskForm):
    
    Amazina =  StringField("Amazina y'umusaruro winjiye", validators=[DataRequired()])
    Taliki = DateField("Tariki winjiriyeho",format='%Y-%m-%d', validators=[DataRequired()])
    Uwagemuye    =  StringField("Amazina y'uwagemuye umusaruro", validators=[DataRequired()])
    Ibiro  =  StringField("Ingano y'ibiro byagemuwe", validators=[DataRequired()])
    Igiciro  =  StringField("Igiciro byagemuweho", validators=[DataRequired()])
    IkiguziCyose  =  StringField("Ikiguzi cyose cyatanzwe", validators=[DataRequired()])
    amafarangaYishyuweKuKiro  =  StringField("Amafaranga yatanzwe ku kiro ", validators=[DataRequired()])
    done_by  =  StringField("Umukono / Uyakiriye", validators=[DataRequired()])
    done_to  =  StringField("Umukono / Uwagemuye", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Emeza')


class ibitaboBankForm(FlaskForm):
    No =  StringField("Amazina y'umusaruro winjiye", validators=[DataRequired()])
    Date = DateField("Tariki winjiriyeho",format='%Y-%m-%d', validators=[DataRequired()])
    Igikorwa    =  StringField("Amazina y'uwagemuye umusaruro", validators=[DataRequired()])
    Debit  =  StringField("Ingano y'ibiro byagemuwe", validators=[DataRequired()])
    Credit  =  StringField("Igiciro byagemuweho", validators=[DataRequired()])
    Solde  =  StringField("Ikiguzi cyose cyatanzwe", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Emeza')



    id = db.Column(db.Integer, primary_key=True, unique=True)
    no = db.Column(db.String(300))
    date = db.Column(db.String(300))
    igikorwa = db.Column(db.String(300))
    debit    = db.Column(db.String(300))
    credit = db.Column(db.String(300))
    solde = db.Column(db.String(300))
    department_id = db.Column(db.String(300), db.ForeignKey('departments.email'))
