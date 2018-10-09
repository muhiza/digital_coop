from flask import render_template, abort
from flask_login import login_required, current_user
from ..models import *
from . import aicos_reporter

def check_coop_admin():
	if not current_user.is_admin:
		abort(403)

def check_admin():
	if not current_user.is_admin:
		abort(403)

@aicos_reporter.route('/')
def home():
	return render_template('dashboardr.html')


@aicos_reporter.route('/eRegistration')
def eRegistration():
	return render_template('eRegistration/eRegistration.html')


@aicos_reporter.route('/cooperative_details/<string:email>', methods=['GET', 'POST'])
@login_required
def coop_details(email):
    #check_admin()

    #check_overall()
    check_coop_admin()
    departments = Department.query.get_or_404(email)
    if departments is not None:
        return render_template("eRegistration/cooperativeDetails.html", 
        						departments=departments, title="Cooperative's details")
    #return redirect(url_for('admin.list_employees'))




"""
@aicos_reporter.route('/eJoining/eJoining.html')
def eJoining():
"""














@aicos_reporter.route('/membersReporter', methods=['GET', 'POST'])
def aicosMemberReporter():
    """
    List all employees
    """
    """
    List all employees
    """
    check_admin()
    check_coop_admin()
    #form = LoginForm()
    # if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
    #apps = Department.query.filter_by(email=current_user.email).first()
    #applications = apps.applications
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    employees_male = employee.members.filter_by(gender='Gabo')
    employees_male_count = employee.members.filter_by(gender='Gabo').count()
    employees_female = employee.members.filter_by(gender='Gole')
    employees_female_count = employee.members.filter_by(gender='Gole').count()
    employees_abatarize = employee.members.filter_by(Amashuri='Abatarize')
    employees_abatarize_count = employee.members.filter_by(Amashuri='Abatarize').count()
    employees_abanza = employee.members.filter_by(Amashuri='Abanza')
    employees_abanza_count = employee.members.filter_by(Amashuri='Abanza').count()
    employees_ayisumbuye = employee.members.filter_by(Amashuri='Ayisumbuye')
    employees_ayisumbuye_count = employee.members.filter_by(Amashuri='Ayisumbuye').count()
    employees_kaminuza = employee.members.filter_by(Amashuri='Kaminuza')
    employees_kaminuza_count = employee.members.filter_by(Amashuri='Kaminuza').count()
    employees_imyuga = employee.members.filter_by(Amashuri='Imyuga')
    employees_imyuga_count = employee.members.filter_by(Amashuri='Imyuga').count()


    employees_amaguru = employee.members.filter_by(Ubumuga='Amaguru')
    employees_amaguru_count = employee.members.filter_by(Ubumuga='Amaguru').count()

    employees_amaboko = employee.members.filter_by(Ubumuga='Amaboko')
    employees_amaboko_count = employee.members.filter_by(Ubumuga='Amaboko').count()


    employees_kutabona = employee.members.filter_by(Ubumuga='Kutabona')
    employees_kutabona_count = employee.members.filter_by(Ubumuga='Kutabona').count()

    employees_kutumva = employee.members.filter_by(Ubumuga='Kutumva')
    employees_kutumva_count = employee.members.filter_by(Ubumuga='Kutumva').count()


    employees_mumutwe = employee.members.filter_by(Ubumuga='Mu mutwe')
    employees_mumutwe_count = employee.members.filter_by(Ubumuga='Mu mutwe').count()


    male_members = employee.members.filter_by(gender='Gole').first()
    male_members_all = employee.members.count()
    employees_count = employee.members.count()
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)

    apps = Department.query.filter_by(email=current_user.email).first()
    applications = apps.applications

    return render_template('members_mgt/members.html',
                           employees=employees,
                           employee=employee, 
                           employees_count=employees_count,
                           male_members=male_members,
                           male_members_all=male_members_all,
                           employees_male=employees_male,
                           employees_female=employees_female,
                           employees_male_count=employees_male_count,
                           employees_female_count=employees_female_count,
                           employees_abatarize=employees_abatarize,
                           employees_abatarize_count=employees_abatarize_count,
                           employees_abanza=employees_abanza,
                           employees_abanza_count=employees_abanza_count,
                           employees_ayisumbuye=employees_ayisumbuye,
                           employees_ayisumbuye_count=employees_ayisumbuye_count,
                           employees_kaminuza=employees_kaminuza,
                           employees_kaminuza_count=employees_kaminuza_count,
                           employees_imyuga=employees_imyuga,
                           employees_imyuga_count=employees_imyuga_count,
                           
                           employees_amaguru=employees_amaguru,
                           employees_amaguru_count=employees_amaguru_count,
                           employees_amaboko=employees_amaboko,
                           employees_amaboko_count=employees_amaboko_count,
                           employees_kutabona=employees_kutabona,
                           employees_kutabona_count=employees_kutabona_count,
                           employees_kutumva=employees_kutumva,
                           employees_kutumva_count=employees_kutumva_count,
                           employees_mumutwe=employees_mumutwe,
                           employees_mumutwe_count=employees_mumutwe_count,
                           #male_members_count=male_members_count,
                           applications=applications,
                           title='Employees')

