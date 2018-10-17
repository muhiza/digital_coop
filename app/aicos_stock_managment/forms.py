from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, IntegerField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional
from ..models import Umusaruro
from . import views


from flask_wtf.file import FileField, FileAllowed, FileRequired


class UmusaruroForm(FlaskForm):
	umwakaWisarura = SelectField("Umwaka W'isarura", choices=[('2018A','2018A')], validators=[DataRequired()])
	amazina = StringField("amazina", validators=[DataRequired(), Length(4, 64)])
	resi = IntegerField("Resi", validators=[DataRequired()], render_kw={"placeholder":"Injiza numero ya resi"})
	zone = StringField("Zone", validators=[DataRequired()], render_kw={"placeholder":"Injiza Zone"})
	umusaruro = IntegerField("Umusaruro", validators=[DataRequired()], render_kw={"placeholder":"Injiza Umusaruro"})
	umuceriWoKurya = IntegerField("Umuceri Wo Kurya", validators=[Optional()], render_kw={"placeholder":"Injiza Umuceri wo kurya (kg)"})
	igiciroCyaKimwe = SelectField("Umusanzu", choices=[('280','280'),('290','290')], validators=[DataRequired()])
	umusanzu = IntegerField("Umusanzu", validators=[DataRequired()], render_kw={"placeholder":"Injiza Umusanzu"})
	amafrwYoGutonoza = IntegerField("Amafaranga Yo Gutonoza", validators=[Optional()], render_kw={"placeholder":"Injiza amafaranga yo gutonoza"})
	submit = SubmitField("Injiza Umusaruro")

	"""
	def validate_resi(self, field):
        if Umusaruro.query.filter_by(resi=field.data).first():
        	raise ValidationError('Resi yawe yarakoreshejwe')
            
    """

class InyongeramusaruroForm(FlaskForm):
	resi = IntegerField("Resi", validators=[DataRequired()], render_kw={"placeholder":"Injiza Resi y'uwahawe Inyongeramusaruro"})
	briquetteKg = FloatField("Briquette", validators=[Optional()], render_kw={"placeholder":"Injiza briquette (kg)"})
	briquettePU = IntegerField("Briquette Kuri inite", validators=[Optional()], render_kw={"placeholder":"Injiza igiciro cya briquette kuri inite (Frw)"})
	DAPandNPKkg = FloatField("DAP & NPK", validators=[DataRequired()], render_kw={"placeholder":"Injiza DAP and NPK (kg)"})
	DAPandNPKpu = IntegerField("DAP & NPK kuri inite", validators=[Optional()], render_kw={"placeholder":"Injiza DAP and NPK  kuri init (Frw)"})
	KCLkg = FloatField("KCL", validators=[Optional()], render_kw={"placeholder":"Injiza KCL (kg)"})
	KCLpu = IntegerField("KCL kuri inite", validators=[Optional()], render_kw={"placeholder":"Injiza KCL kuri inite (Frw)"})
	ImbutoKg = FloatField("Imbuto", validators=[Optional()], render_kw={"placeholder":"Injiza Imbuto (kg)"})
	ImbutoPU = IntegerField("Imbuto kuri inite", validators=[Optional()], render_kw={"placeholder":"Injiza Imbuto kuri inite (Frw)"})
	ImifukaKg = FloatField("Imifuka", validators=[Optional()], render_kw={"placeholder":"Injiza Imifuka uko ingana"})
	ImifukaPU = IntegerField("Imifuka yishyuwe", validators=[Optional()], render_kw={"placeholder":"Injiza Imifuka kuri umwe (Frw)"})
	redevenceUbuso = FloatField("Redevence", validators=[Optional()], render_kw={"placeholder":"Injiza redevence ubuso"})
	redevencePU = IntegerField("Redevence kuri inite", validators=[Optional()], render_kw={"placeholder":"Injiza Redevence kuri unite (Frw)"})
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
