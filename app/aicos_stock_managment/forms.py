from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, IntegerField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField, FloatField
from wtforms.fields.html5 import DateField, NumberInput
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional
from ..models import Umusaruro
from . import views


from flask_wtf.file import FileField, FileAllowed, FileRequired


class UmusaruroForm(FlaskForm):
	umwakaWisarura = SelectField("Umwaka W'isarura", choices=[('2018A','2018A')], validators=[Optional()])
	amazina = StringField("amazina", validators=[Optional(), Length(4, 64)])
	resi = IntegerField("Resi", validators=[Optional()], render_kw={"placeholder":"Injiza numero ya resi y'umunyamuryango"})
	zone = StringField("Zone", validators=[Optional()], render_kw={"placeholder":"Injiza Zone"})
	umusaruro = IntegerField("Umusaruro", validators=[Optional()], render_kw={"placeholder":"Injiza Umusaruro Wabonetse wose"})
	umuceriWoKurya = IntegerField("Umuceri Wo Kurya", validators=[Optional()], render_kw={"placeholder":"Injiza Umuceri wo kurya (kg)"})
	igiciroCyaKimwe = SelectField("Igiciro Cya Kimwe(Frw/kg)", choices=[('290','290'),('280','280')], validators=[Optional()])
	umusanzu = SelectField("Umusanzu Ku kiro (Frw/kg)", choices=[('15','15')], validators=[Optional()])
	amafrwYoGutonoza = SelectField("Amafaranga yo gutonoza (Frw/kg)", choices=[('50','50')], validators=[Optional()])
	submit = SubmitField("Injiza Umusaruro")

	"""
	def validate_resi(self, field):
        if Umusaruro.query.filter_by(resi=field.data).first():
        	raise ValidationError('Resi yawe yarakoreshejwe')
            
    """

class InyongeramusaruroForm(FlaskForm):
	umwakaWisarura = SelectField("Umwaka W'isarura", choices=[('2018A','2018A')], validators=[Optional()])
	resi = IntegerField("Resi", validators=[Optional()], render_kw={"placeholder":"Injiza Resi y'uwahawe Inyongeramusaruro"})
	briquetteKg = FloatField("Briquette", validators=[Optional()], render_kw={"placeholder":"Injiza briquette (kg)"})
	briquettePU = SelectField("Briquette kuri kiro (Frw)", choices=[('390','390')], validators=[Optional()])
	DAPandNPKkg = FloatField("DAP & NPK", validators=[Optional()], render_kw={"placeholder":"Injiza DAP and NPK (kg)"})
	DAPandNPKpu = SelectField("Igiciro kuri DAP & NPK", choices=[('430','430')], validators=[Optional()])
	KCLkg = FloatField("KCL", validators=[Optional()], render_kw={"placeholder":"Injiza KCL (kg)"})
	KCLpu = SelectField("Igiciro kuri KCL", choices=[('395','395')], validators=[Optional()])
	ImbutoKg = FloatField("Imbuto", validators=[Optional()], render_kw={"placeholder":"Injiza Imbuto (kg)"})
	ImbutoPU = SelectField("Igiciro ku Mbuto", choices=[('400','400')], validators=[Optional()])
	ImifukaKg = IntegerField("Imifuka", widget=NumberInput(), validators=[Optional()], render_kw={"placeholder":"Injiza Imifuka uko ingana"})
	ImifukaPU = SelectField("Igiciro ku mufuka", choices=[('400','400')], validators=[Optional()])
	redevenceUbuso = FloatField("Redevence", validators=[Optional()], render_kw={"placeholder":"Injiza redevence ubuso"})
	redevencePU = SelectField("Redevence kuri inite", choices=[('250','250')], validators=[Optional()])
	submit = SubmitField("Injiza Inyongeramusaruro")

class IbyakoreshejweForm(FlaskForm):
	resi = IntegerField("Resi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Resi y'uwahawe Ibyakoreshejwe"})
	beamSup = IntegerField("Beam and Sup", validators=[Optional()], render_kw={"placeholder":"Injiza Beam and Sup"})
	ibihanoCoop = IntegerField("Ibihano bya koperative", validators=[Optional()], render_kw={"placeholder":"Injiza Ibihano by cooperative"})
	APIISAMAKIbihano = IntegerField("ibihano bya APIISAMAK", validators=[Optional()], render_kw={"placeholder":"Injiza Ibihano by APIISAMAK"})
	ibiraraneNPKandUREA = IntegerField("ibirarane bya NPK na UREA", validators=[Optional()], render_kw={"placeholder":"Injiza Ibirarane by NPK na UREA"})
	umusoro = IntegerField("Umusoro", validators=[Optional()], render_kw={"placeholder":"Injiza umusoro watanzwe"})
	kwishyuraItsinda = IntegerField("Kwishyura itsinda", validators=[Optional()], render_kw={"placeholder":"Injiza Ubwishyu bw'itsinda"})
	Sheeting = IntegerField("Kwishyura itsinda", validators=[Optional()], render_kw={"placeholder":"Injiza Ubwishyu bw'itsinda"})
	PIS = IntegerField("P/S", validators=[Optional()], render_kw={"placeholder":"Injiza P|S"})
	umuceriYagurijweUmwakaKUshize = IntegerField("Umuceri Yagurijwe ubushize", validators=[Optional()], render_kw={"placeholder":"Injiza Umuceri yagurijwe Umwaka ushize"})
	ibindi = IntegerField("Ibindi", validators=[Optional()], render_kw={"placeholder":"Injiza Ibindi yasabwe"})
	submit = SubmitField("Injiza Ibyakoreshejwe")


class KonteZaBankForm(FlaskForm):
	resi = IntegerField("Resi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Resi y'uwahawe Ibyakoreshejwe"})
	izinaryaNyiriKonte = StringField("Amazina ya nyirayo", validators=[DataRequired()], render_kw={"placeholder":"Injiza izina rya nyiri konte"})
	izanaRyaBank = StringField("Izina Rya Banki", validators=[DataRequired()], render_kw={"placeholder":"Injiza izina rya banki"})
	numeroYaKonte = StringField("No ya Konte", validators=[DataRequired()], render_kw={"placeholder":"Injiza nimero ya konte"})
	submit = SubmitField("Injiza Konte")
