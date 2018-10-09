from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_members
from flask_login import current_user, login_required
from ..models import * 
from .forms import *
import flask_excel
import flask_excel as excel

import nexmo

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)





client = nexmo.Client(key='e7096025', secret='ab848459dae27b51')



def check_admin():
    #form = LoginForm()
    # departments = Employee.query.filter_by(email=form.email.data).first()
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        #if not current_user.
        abort(403)


def check_overall():
    if not current_user.is_overall:
        abort(403)




def check_coop_admin():
    if not current_user.is_coop_admin:
        abort(403)


@aicos_members.route('/', methods=['GET', 'POST'])
def aicos_members_home():
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





    
    employees_male = employee.members.filter_by(Igitsina='male')
    employees_male_count = employee.members.filter_by(Igitsina='male').count()
    employees_female = employee.members.filter_by(Igitsina='female')
    employees_female_count = employee.members.filter_by(Igitsina='female').count()




    employees_abatarize = employee.members.filter_by(Amashuri='no')
    employees_abatarize_count = employee.members.filter_by(Amashuri='no').count()
    employees_abanza = employee.members.filter_by(Amashuri='low')
    employees_abanza_count = employee.members.filter_by(Amashuri='low').count()
    employees_ayisumbuye = employee.members.filter_by(Amashuri='medium')
    employees_ayisumbuye_count = employee.members.filter_by(Amashuri='medium').count()
    employees_kaminuza = employee.members.filter_by(Amashuri='high')
    employees_kaminuza_count = employee.members.filter_by(Amashuri='high').count()
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


    male_members = employee.members.filter_by(Igitsina='Gole').first()
    #male_members_all = male_members.query.all()
    employees_count = employee.members.count()
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)

    apps = Department.query.filter_by(email=current_user.email).first()
    applications = apps.applications

    return render_template('indexz.html',
                           employees=employees,
                           employee=employee, 
                           employees_count=employees_count,
                           male_members=male_members,
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



@aicos_members.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
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
    employees_count = employee.members.count()

    notes = Notification.query.filter_by(department_id=current_user.email)



    employees_male = employee.members.filter_by(Igitsina='male')
    employees_male_count = employee.members.filter_by(Igitsina='male').count()
    employees_female = employee.members.filter_by(Igitsina='female')
    employees_female_count = employee.members.filter_by(Igitsina='female').count()
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


    male_members = employee.members.filter_by(Igitsina='Gole').first()
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)

    apps = Department.query.filter_by(email=current_user.email).first()
    applications = apps.applications

    return render_template('home.html',
                           employees=employees,
                           employee=employee,
                           employees_count=employees_count,
                           notes = notes,


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
                           applications=applications,
                           title='Employees')






@aicos_members.route('/memberDetails/<int:id>', methods=['GET', 'POST'])
@login_required
def memberDetails(id):
    check_admin()
    employee = Member.query.get_or_404(id)

    #motos = employee.motos
    if employee is not None:
        return render_template("member_details.html", employee=employee)
    return redirect(url_for('aicos_members.aicos_members_home'))





# Views for the full details of a specific employee
@aicos_members.route('/cooperative_details/heree')
@login_required
def cooper_det():
    #check_admin()
    #check_overall()
    #check_coop_admin()
    #departments = Department.query.get_or_404(ema0il)
    departmentszx = Department.query.filter_by(email=current_user.email).first()
        
    employees_male_count = departmentszx.members.filter_by(Igitsina='Gabo').count()
    employees_female_count = departmentszx.members.filter_by(Igitsina='Gole').count()

    if departmentszx is not None:
      return render_template("deta/coop_det.html", departmentszx=departmentszx, employees_male_count=employees_male_count,
                               employees_female_count=employees_female_count,
            title="Cooperative's details")
    #return redirect(url_for('admin.list_employees'))


@aicos_members.route('/memberPayments')
def memberPayments():
    goals = Goal.query.all()
    return render_template("payments/payment_list.html", goals=goals)



@aicos_members.route('/memberPayments/Goals', methods=['GET', 'POST'])
def goalPayments():
    form = GoalForm()
    if form.validate_on_submit():
        newGoal = Goal (
                        name = form.name.data,
                        Description = form.description.data,
                        Amount = form.amount.data,
                        startingDate = form.startingDate.data,
                        endingDate = form.endingDate.data
                        )
        try:
             db.session.add(newGoal)
             db.session.commit()
             flash("Umuaze kwandika ikindi gikorwa neza!")
             return redirect(url_for('aicos_members.memberPayments'))
        except Exception:
            flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
    return render_template("payments/goals/newGoal.html", form=form)





@aicos_members.route('/memberPayments/Goals/Delete/<int:id>')
def goalDelete(id):
    goal = Goal.query.get_or_404(id)
    db.session.delete(goal)
    db.session.commit()
    flash("Umuaze gusiba igikora neza")
    return redirect(url_for('aicos_members.memberPayments'))






@aicos_members.route('/joiningCharts')
def joiningChart():
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    employees_male = employee.members.filter_by(Igitsina='Gabo')
    employees_male_count = employee.members.filter_by(Igitsina='Gabo').count()
    employees_female = employee.members.filter_by(Igitsina='Gole')
    employees_female_count = employee.members.filter_by(Igitsina='Gole').count()
    male_members = employee.members.filter_by(Igitsina='Gole').first()
    male_members_all = male_members.query.all()
    employees_count = employee.members.count()
    return render_template("employees/joining_chart.html",
                            employees=employees,
                            employee=employee, 
                            employees_count=employees_count,
                            male_members=male_members,
                            male_members_all=male_members_all,
                            employees_male=employees_male,
                            employees_female=employees_female,
                            employees_male_count=employees_male_count,
                            employees_female_count=employees_female_count)





@aicos_members.route('/create')
def memberCreate():
    return render_template("create/create.html")







# The view to list all role Views
@aicos_members.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.filter_by(department_id=current_user.email)
    return render_template('roles/roles.html',
                           roles=roles, title='Roles')






# Function for adding new role
@aicos_members.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role(*args, **kwargs):
    """
    Add a role to the database
    """
    check_admin()
    add_role = True
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data,
                    department_id = current_user.email)
        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.list_roles'))
    # load role template
    return render_template('roles/role.html', add_role=add_role,
                           form=form, title='Add Role')





# The view to list all staff Views
@aicos_members.route('/staffs')
@login_required
def list_staffs():
    check_admin()
    """
    List all roles
    """
    staffs = Staff.query.filter_by(department_id=current_user.email)
    return render_template('roles/staffs.html',
                           staffs=staffs, title='Staffs')


# Function for adding new role
@aicos_members.route('/staff/add', methods=['GET', 'POST'])
@login_required
def add_staff(*args, **kwargs):
    """
    Add a role to the database
    """
    check_admin()
    add_staff = True
    form = StaffForm()
    if form.validate_on_submit():
        staff = Staff(

                      first_name=form.firstName.data,
                      last_name=form.lastName.data,
                      nid=form.Nid.data,
                      district=form.District.data,
                      sector=form.Sector.data,
                      sex=form.Sex.data,
                      yob=form.Yob.data,
                      position=form.Position.data,
                      education=form.Education.data,
                      telephone=form.Telephone.data,
                      email=form.Email.data,
                      monthly_net_salary=form.monthlyNetSalary.data,
                      department_id = current_user.email
                      )
        try:
            # add role to the database
            db.session.add(staff)
            db.session.commit()
            flash('You have successfully added a new staff member.')
        except:
            # in case role name already exists
            flash('Error: Staff name already exists.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.list_staffs'))
    # load role template
    return render_template('roles/staff.html', add_staff=add_staff,
                           form=form, title='Add Role')









# The view to list all role Views
@aicos_members.route('/activities')
@login_required
def list_activities():
    check_admin()
    """
    List all roles
    """
    activities = Activity.query.filter_by(department_id=current_user.email)
    return render_template('roles/activities.html',
                           activities=activities, title='Activities')



# Function for adding new role
@aicos_members.route('/activity/add', methods=['GET', 'POST'])
@login_required
def add_activity(*args, **kwargs):
    """
    Add a role to the database
    """
    check_admin()
    add_activity = True
    form = ActivityForm()
    if form.validate_on_submit():
        activity = Activity(
                            name=form.name.data,
                            description=form.description.data,
                            department_id = current_user.email)
        try:
            # add role to the database
            db.session.add(activity)
            db.session.commit()
            flash('You have successfully added a new activity.')
        except:
            # in case role name already exists
            flash('Error: activity name already exists.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.list_activities'))
    # load role template
    return render_template('roles/activity.html', add_activity=add_activity,
                           form=form, title='Add Role')







# The view to list all role Views
@aicos_members.route('/assets')
@login_required
def list_assets():
    check_admin()
    """
    List all roles
    """
    assets = Asset.query.filter_by(department_id=current_user.email)
    return render_template('roles/assets.html',
                           assets=assets, title='Activities')



# Function for adding new role
@aicos_members.route('/asset/add', methods=['GET', 'POST'])
@login_required
def add_asset(*args, **kwargs):
    """
    Add a role to the database
    """
    check_admin()
    add_asset = True
    form = AssetForm()
    if form.validate_on_submit():
        asset = Asset(
                            asset_type=form.assetType.data,
                            asset_location=form.assetLocation.data,
                            asset_value=form.assetValue.data,
                            description=form.description.data,
                            department_id = current_user.email)
        try:
            # add role to the database
            db.session.add(asset)
            db.session.commit()
            flash('You have successfully added a new asset.')
        except:
            # in case role name already exists
            flash('Error: asset name already exists.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.list_assets'))
    # load role template
    return render_template('roles/asset.html', add_asset=add_asset,
                           form=form, title='Add Role')












@aicos_members.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()
    add_role = False
    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.list_roles'))
    form.description.data = role.description
    form.name.data = role.name
    return render_template('roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


















@aicos_members.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')
    # redirect to the roles page
    return redirect(url_for('aicos_members.list_roles'))
    return render_template(title="Delete Role")











































# The view to list all role Views
@aicos_members.route('/reports')
@login_required
def list_reports():
    check_admin()
    """
    List all roles
    """
    reports = Report.query.all()
    return render_template('tools/reports/reports.html',
                           reports=reports, title='Reports')






# Function for adding new role
@aicos_members.route('/reports/add', methods=['GET', 'POST'])
@login_required
def add_report(*args, **kwargs):
    """
    Add a role to the database
    """
    check_admin()
    add_report = True
    form = ReportForm()
    if form.validate_on_submit():
        report = Report(status=form.status.data,
                        project=form.project.data,
                        task=form.task.data,
                        description=form.description.data,
                        notes=form.notes.data)
        try:
            # add role to the database
            db.session.add(report)
            db.session.commit()
            flash('You have successfully created a report.')
        except:
            # in case role name already exists
            flash('Error:  the report is not valid.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.list_reports'))
    # load role template
    return render_template('tools/reports/report.html', add_report=add_report,
                           form=form, title='Add Report')

@aicos_members.route('/report/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_report(id):
    """
    Edit a role
    """
    check_admin()
    add_report = False
    report = Report.query.get_or_404(id)
    form = ReportForm(obj=report)
    if form.validate_on_submit():
        report.status = form.status.data
        report.project = form.project.data
        report.task = form.task.data
        report.description = form.description.data
        report.notes = form.notes.data
        db.session.add(report)
        db.session.commit()
        flash('You have successfully edited the report.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.list_reports'))
    form.notes.data = report.notes
    form.description.data = report.description
    form.task.data = report.task
    form.project.data = report.project
    form.status.data = report.status
    return render_template('tools/reports/report.html', add_report=add_report,
                           form=form, title="Edit Report")

@aicos_members.route('/report/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_report(id):
    """
    Delete a role from the database
    """
    check_admin()
    report = Report.query.get_or_404(id)
    db.session.delete(report)
    db.session.commit()
    flash('You have successfully deleted the report.')
    # redirect to the roles page
    return redirect(url_for('aicos_members.list_reports'))
    return render_template(title="Delete Report")









# This is the views for listing all the decisions
@aicos_members.route('/cooperative/decisions')
def decisions_list():
    decisions = Decision.query.all()
    return render_template("tools/decisions_list.html", decisions=decisions, title="List of decisions")








# Function for adding new role
@aicos_members.route('/payment/add', methods=['GET', 'POST'])
@login_required
def add_payment(*args, **kwargs):
    """
    Add a role to the database
    """
    check_admin()
    add_payment = True
    form = PaymentForm()
    if form.validate_on_submit():
        payment = Payment(reason=form.name.data,
                        amount = form.amount.data,
                        date    = form.date.data,
                        d=form.description.data)
        try:
            # add role to the database
            db.session.add(payment)
            db.session.commit()
            flash('You have successfully added a new payment.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.list_roles'))
    # load role template
    return render_template('payments/new_payment.html', add_payment=add_payment,
                           form=form, title='Add Payment')






















# This is the views for adding new decision
@aicos_members.route('/cooperative/create/decision', methods=['GET', 'POST'])
@login_required
def create_decision():
    check_admin()
    form = DecForm()
    if form.validate_on_submit():
        dec = Decision(status=form.status.data,
                        decision=form.decision.data,
                        owner   = form.owner.data,
                        stakeholders=form.stakeholders.data,
                        due_date=form.due_date.data,
                        background = form.background.data,
                        department_id = current_user.email)

        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(dec)
            db.session.add(notif)
            db.session.commit()
            flash("You have successfully created a decision")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_members.decisions_list'))
    return render_template("tools/create_decision.html", form=form, title="Create")





# This is the view for the how-to-article for the members of the cooperatives (Just for the guiding them)
@aicos_members.route('/cooperative/how_to_articles_list', methods=['GET', 'POST'])
def how_to_list():
    howtos = Howto.query.all()
    return render_template("tools/how_to/how_to_list.html", howtos=howtos, title="How to lists")
    


@aicos_members.route('/cooperative/create/how_to_article', methods=['GET', 'POST'])
def create_how_to():
    check_admin()
    form = HowtoForm()
    if form.validate_on_submit():
        howto = Howto    (name=form.name.data,
                        labels=form.labels.data,
                        description = form.description.data,
                        steps=form.steps.data,
                        file=form.file.data)


        notif = Notification(action="Wrote a how to article",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(howto)
            db.session.add(notif)
            db.session.commit()


            to_number = '+250786012383'
            message = current_user.email + 'Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]



            flash("You have successfully created an article")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_admin.how_to_list'))
    return render_template("tools/how_to/create_how_to.html", form=form, title="Create How to list")





# This is the view for the links which are shared with members and all other stuff related to it anyway.
@aicos_members.route('/cooperative/shared_links', methods=['GET', 'POST'])
def links_list():
    links = Link.query.all()
    return render_template("tools/links/links_list.html", links=links, title="Shared links list")
    


@aicos_members.route('/cooperative/create/share_a_link', methods=['GET', 'POST'])
def create_link():
    check_admin()
    form = LinkForm()
    if form.validate_on_submit():
        link = Link    (link=form.link.data,
                        title=form.title.data,
                        labels = form.labels.data,
                        sharewith=form.sharewith.data,
                        comment=form.comment.data)

        notif = Notification(action="Shared a link",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(link)
            db.session.add(notif)
            db.session.commit()

            to_number = '+250786012383'
            message = current_user.email + 'Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

            flash("You have successfully shared a link")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_members.links_list'))
    return render_template("tools/links/create_link.html", form=form, title="Create How to list")







@aicos_members.route('/cooperative/create/share_a_file', methods=['GET', 'POST'])
def create_file():
    check_admin()
    form = FileForm()
    if form.validate_on_submit():
        filename = images.save(request.files['recipe_image'])
        url = images.url(filename)
        file = File    (form.name.data,
                        form.description.data,
                        True,
                        filename,
                        url)
        notif = Notification(action="Shared a file",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(file)
            db.session.add(notif)
            db.session.commit()

            to_number = '+250786012383'
            message = current_user.email + 'Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            flash("You have successfully shared a file")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_members.links_list'))
    return render_template("tools/file/shareFile.html", form=form, title="Share Files")



@aicos_members.route('/cooperative/shared_files', methods=['GET', 'POST'])
def files_list():
    files = File.query.all()
    return render_template("tools/file/filesList.html", files=files, title="Shared files list")





# This is the view to list all the members.
@aicos_members.route('/cooperative/members', methods=['GET', 'POST'])
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()
    check_coop_admin()
    #form = LoginForm()
    # if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
    apps = Department.query.filter_by(email=current_user.email).first()
    applications = apps.applications
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)
    return render_template('employees/employees.html',
                           employees=employees, applications=applications, apps=apps,
                           employee=employee, title='Employees')

    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')


# Views for the full details of a specific employee
@aicos_members.route('/member_details/<int:id>', methods=['GET', 'POST'])
@login_required
def member_details(id):
    check_admin()
    employee = Member.query.get_or_404(id)
    if employee is not None:
        return render_template("employees/employee_details.html", employee=employee)
    return redirect(url_for('aicos_members.list_employees'))






# This is the view which is used to import all the members from excel sheets
# This is the view used to import all the cooperatives from excel sheet.
SQLALCHEMY_DATABASE_URI = 'mysql://root:annemuhiza@localhost/coop'
@aicos_members.route("/importmbs", methods=['GET', 'POST'])
def doimportmbs():
    add_member = False
    upload_file = True
    if request.method == 'POST':
        def mbs_init_func(row):
            m = Member(row['sno'])

            m.id = row['id']
            m.sno = row['sno']
            m.izina_ribanza = row['izina_ribanza']
            m.izina_rikurikira = row['izina_rikurikira']
            m.Ayandi = row['Ayandi']
            m.Igitsina = row['Igitsina']
            m.Indangamuntu = row['Indangamuntu']
            m.tariki_yavukiye = row['tariki_yavukiye']
            m.Intara = row['Intara']
            m.Akarere = row['Akarere']
            m.Umurenge = row['Umurenge']
            m.Akagari = row['Akagari']
            m.Umudugudu = row['Umudugudu']
            m.tariki_yinjiriye = row['tariki_yinjiriye']
            m.umugabane_ukwezi = row['umugabane_ukwezi']
            m.Umukono = row['Umukono']
            m.nomero_telephone = row['nomero_telephone']
            m.Amashuri = row['Amashuri']
            m.Ubumuga = row['Ubumuga']
            m.Arubatse = row['Arubatse']
            m.umubare_abana = row['umubare_abana']
            m.icyiciro_ubudehe = row['icyiciro_ubudehe']
            m.Ubwishingizi = row['Ubwishingizi']
            m.akazi_akora_muri_koperative = row['akazi_akora_muri_koperative']
            m.akazi_akora_ahandi = row['akazi_akora_ahandi']
            m.ubuso_ahingaho = row['ubuso_ahingaho']
            m.ubwoko_igihingwa = row['ubwoko_igihingwa']
            m.ubuso_ahingaho_ibindi = row['ubuso_ahingaho_ibindi']
            m.ubwoko_igihingwa_kindi = row['ubwoko_igihingwa_kindi']
            m.ubuso_budakoreshwa = row['ubuso_budakoreshwa']
            m.department_id = current_user.email



            #m.name = row['names']
            #m.plate = row['plate']
            #m.Owner = row['Owner']
            #m.department_id = row['department_id']
            #c.id = row['id']
            return m
        #try:
        request.save_book_to_database(
            field_name='file', session=db.session,
            tables=[Member],
            initializers=[mbs_init_func])
          #return redirect(url_for('.handson_table'), code=302)
          #flash("Lisiti y'abanyamuryango ba Cooperative yinjiye neza muri sisiteme!")
        #except:
         # flash("The list you are uploading is not well formated, please reformat it and try again or Download the sample sheet")
        return redirect(url_for('aicos_members.aicos_members_home'), code=302)
    return render_template("employees/upload.html", 
                            add_member=add_member,
                            upload_file=upload_file,
                            title="Upload a file")


@aicos_members.route("/members_template", methods=['GET'])
def templateDownload():
    query_sets = Member.query.filter_by(id=20).all()
    column_names = ['id', 'firstName', 'secondName', 'others',
                    'Province','District','Sector','Cell',
                    'nId', 'entryDate', 'share', 'exitDate',
                    'umuzungura', 'umukono', 'gender', 'dob', 'age', 'phone',
                    'Amashuri', 'Ubumuga', 'marital_status', 'ubudehe', 'insurance', 'Language',
                    'role_id', 'department_id', 'has_children', 'rular_or_urban', 'is_active',
                    'member_source', 'job']
    return excel.make_response_from_query_sets(query_sets, column_names, "xls")








# This is the function for adding the new members in the cooperative.
@aicos_members.route('/cooperative/create/new_member', methods=['GET', 'POST'])
@login_required
def AddNewMember():
    check_admin()
    add_member = True
    upload_file = False
    form = MemberForm()
    if form.validate_on_submit():
        NewMember = Member(
                          izina_ribanza = form.izina_ribanzax.data,
                          izina_rikurikira = form.izina_rikurikirax.data,
                          Ayandi     = form.ayandix.data,
                          Igitsina  = form.igitsinax.data,
                          Indangamuntu  = form.indangamuntux.data,
                          #Code          = form.code.data,
                          tariki_yavukiye = form.tariki_yavukiyex.data,
                          Intara = form.intarax.data,

                          Akarere = form.akarerex.data,
                          Umurenge     = form.umurengex.data,
                          Akagari     = form.akagarix.data,
                          Umudugudu     = form.umudugudux.data,
                          tariki_yinjiriye     = form.tariki_yinjiriyex.data,
                          umugabane_ukwezi = form.umugabanex.data,

                          Umukono    = form.umukonox.data,
                          nomero_telephone  = form.nomero_ya_telephonex.data,
                          Amashuri  = form.amashurix.data,
                          Ubumuga  = form.ubumugax.data,

                          Arubatse     = form.arubatsex.data,
                          umubare_abana     = form.umubare_wabanax.data,
                          icyiciro_ubudehe = form.icyiciro_cyubudehex.data,
                          Ubwishingizi    = form.ubwishingizix.data,
                          akazi_akora_muri_koperative  = form.akazi_akora_muri_koperativex.data,
                          akazi_akora_ahandi  = form.akandi_kazi_akorax.data,

                          ubuso_ahingaho  = form.ubuso_ahingahox.data,
                          ubwoko_igihingwa  = form.ubwoko_bwigihingwax.data,
                          ubuso_ahingaho_ibindi = form.ubuso_ahingaho_ibindix.data,
                          
                          ubwoko_igihingwa_kindi = form.ubwoko_bwigihingwa_kindix.data,
                          ubuso_budakoreshwa = form.ubuso_budakoreshwax.data,
                          department_id = current_user.email
                          )

        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            """
            to_number = '+250786012383'
            message = 'You have been added in the cooperative'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            """
            db.session.add(NewMember)
            db.session.add(notif)
            db.session.commit()
    

            flash("Umaze kwindika umunyamuryango neza muri sisiteme")
        except:
            flash("Amakuru watanze ntago yashoboye kwinjira muri sisiteme!")
        return redirect(url_for('aicos_members.aicos_members_home'))
    return render_template("employees/membership_form.html", form=form,
                            add_member=add_member,
                            upload_file=upload_file,
                            title="Add New Member")






# This is the view for list all reports
@aicos_members.route('/admin/cooperative/reports')
def reports_list():
    reports = Report.query.all()
    return render_template("tools/reports_list.html", reports=reports, title="List of reports")

@aicos_members.route('create/report', methods=['GET', 'POST'])
@login_required
def create_report():
    check_admin()
    form = RepForm()
    if form.validate_on_submit():
        rep = Report(status=form.status.data,
                        report_name=form.report_name.data,
                        owner   = form.owner.data,
                        stakeholders=form.stakeholders.data,
                        created_date=form.created_date.data,
                        description = form.description.data,
                        department_id = current_user.email)


        notif = Notification(action="Created a report",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            to_number = '+250786012383'
            message = current_user.email + ' added 300 frw to your contribution account, new balance is 6000 frw.'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]


            db.session.add(rep)
            db.session.add(notif)
            db.session.commit()

            flash("You have successfully created a report")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_members.reports_list'))
    return render_template("tools/create_report.html", form=form, title="Create")


# This is the view for the meeting noted in the cooperatives.

@aicos_members.route('/cooperative/create/meeting_notes', methods=['GET', 'POST'])
@login_required
def create_meeting_notes():
    check_admin()
    form = MeetingNotesForm()
    if form.validate_on_submit():
        dec = Decision(status=form.status.data,
                        decision=form.decision.data,
                        owner   = form.owner.data,
                        stakeholders=form.stakeholders.data,
                        due_date=form.due_date.data,
                        background = form.background.data,
                        department_id = current_user.email)


        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(dec)
            db.session.add(notif)
            db.session.commit()


            to_number = '+250786012383'
            message = current_user.email + 'Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]



            flash("You have successfully approved a member")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_members.decisions_list'))
    return render_template("tools/create_decision.html", form=form, title="Create")


@aicos_members.route('/admin/cooperative/contributions')
def contributions_list():
    contributions = Contribution.query.all()
    return render_template("tools/contributions_list.html", 
        contributions=contributions, title="List of Contributions")

@aicos_members.route('/cooperative/add/contribution', methods=['GET', 'POST'])
@login_required
def add_contribution():
    check_admin()
    form = contributionForm()
    if form.validate_on_submit():
        cont = Contribution(
                        owner=form.contributor.data,
                        contributionFor=form.contributionFor.data,
                        amount   = form.amount.data,
                        comment=form.comment.data,
                        department_id = current_user.email)
        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            to_number = '+250786012383'
            message = current_user.email + ' Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

            db.session.add(cont)
            db.session.add(notif)
            db.session.commit()
            flash("You have successfully saved contribution")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_members.contributions_list'))
    return render_template("tools/add_contribution.html", form=form, title="Add contribution")




@aicos_members.route('/cooperative/contributions/report')
def pdf_template():
    contributions = Contribution.query.all()
    date = datetime.datetime.now()
    rendered = render_template('tools/pdf_template.html',
        contributions=contributions, date=date)
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response





@aicos_members.route('/admin/cooperative/communications')
def communications_list():
    communications = Communication.query.all()
    return render_template("tools/communications_list.html", 
        communications=communications, title="List of recent Communication")

@aicos_members.route('/cooperative/add/communication', methods=['GET', 'POST'])
@login_required
def add_communication():
    check_admin()
    form = communicationForm()
    if form.validate_on_submit():
        com = Communication(

                        ms_from=form.ms_from.data,
                        to=form.to.data,
                        message=form.message.data,
                        comment   = form.comment.data,
                        department_id = current_user.email)

        notif = Notification(action="Communication",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            to_number = '+250786012383'
            message = current_user.email + ' Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

            db.session.add(com)
            db.session.add(notif)
            db.session.commit()
            flash("You have successfully send a message")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_members.communications_list'))
    return render_template("tools/add_communication.html", form=form, title="Add Communication")



# Deal with the members who want to join the cooperative here
@aicos_members.route('/members/applied')
@login_required
def list_applications():
    check_admin()
    apps = Department.query.filter_by(email=current_user.email).first()
    applications = apps.applications
    return render_template("employees/applied_members.html", apps=apps, applications=applications,
                            title="List of applied members")

# View for details of applicant members
@aicos_members.route('members/applicant/<int:id>/details', methods=['GET', 'POST'])
@login_required
def applicant_details(id):
    check_admin()
    applicant = Application.query.get_or_404(id)
    if applicant is not None:
        return render_template("employees/applicant_details.html", applicant=applicant, title="Applicant Details")
"""
# Adding new member in the department
@admin.route('/employee/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    check_admin()
    form = NewEmployee()
    if form.validate_on_submit():
        employee = Member(email=form.email.data,
                           username=form.username.data,
                            first_name=form.FirstName.data,
                            last_name=form.LastName.data,
                            department_id=current_user.email)
        try:
            db.session.add(employee)
            db.session.commit()
            flash("You have added new member")
            return redirect(url_for('admin.list_employees'))
        except:
            flash("The member is already exist")
    return render_template("admin/employees/add_employee.html", form=form, title="Add New employee")
"""

@aicos_members.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id, *args):
    """
    Assign a department and a role to an employee
    """
    check_admin()
    employee = Member.query.get_or_404(id)
    # prevent admin from being assigned a department or role
    #if employee.is_admin:
        #abort(403)
    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.department = form.cooperative.data
        employee.role = form.role.data
        employee.department_id = current_user.email
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a department and role.')
        # redirect to the roles page
        return redirect(url_for('aicos_members.aicos_members_home'))
    return render_template('employees/employee.html', employee=employee, form=form, *args)

# Views for deleting the member from the cooperative
@aicos_members.route('/member/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete_member(id):
    check_admin()
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    flash("You have successgully removed a member from your cooperative")
    return redirect(url_for('aicos_members.aicos_members_home'))
    return render_template(title="Delete a member")

# The view to confirm the applied members to join their respective cooperatives.
@aicos_members.route('/member/confirmed/<int:id>', methods=['GET', 'POST'])
@login_required
def confirm_member(id):
    check_admin()
    app = Application.query.get_or_404(id)
    memb = Employee(email=app.email,
                      username=app.others,
                      first_name=app.first_name,
                      last_name=app.last_name,
                      department_id=current_user.email)
    
    try:
        #db.session.add(memb)
        #db.session.commit()
        app = Application.query.get_or_404(id)
        emp = Employee.query.filter_by(email=app.email).first()
        #admin = User.query.filter_by(username='admin').first()
        emp.department_id = current_user.email
        db.session.commit()
        appz = Application.query.get_or_404(id)
        db.session.delete(appz)
        db.session.commit()
        #to_number = request.form['to_number']
        to_number = '+250786012383'
        message = current_user.email + ' Has approved your Application,Your RegNo is RW00247'
        response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
        response_text = response['messages'][0]
        flash("You have successfully approved a member")
    except:
        flash("The member already exist")
    return redirect(url_for('aicos_members.list_employees'))
    return render_template(title="You have successfully approved a member")

# View to Sending envitations to people to join the cooperative.
@aicos_members.route('/members/invite')
def invite_members():
    members = Employee.query.filter_by(department_id=None)
    inveted_by = Employee.query.filter_by(invited_by=current_user.email)
    #all_member = members.department_id
    #return redirect(url_for('aicos_members.list_employees'))
    return render_template("home/invite_members.html", members=members, title="Invite members to join the cooperative")

@aicos_members.route('/member/add/<int:id>', methods=['GET', 'POST'])
def add_member(id):
    members = Member.query.get_or_404(id)
    members.department_id = current_user.email
    db.session.commit()
    flash("Member has been added successifully, Add more")
    return redirect(url_for('aicos_members.invite_members'))
    #return render_template("home/invite_members.html", members=members, title="Invite members to join the cooperative")

@aicos_members.route('/member/invite/<int:id>', methods=['GET', 'POST'])
def invite(id):
    member = Employee.query.get_or_404(id)
    member.is_invited = True
    member.invited_by = current_user.email
    db.session.commit()
    flash("Member, " + str(member.username) + " Has been invited successifully, Invite more")
    return redirect(url_for('aicos_members.invite_members'))

"""
# The view to set one member of the cooperative as the cooperative member from other members and them manage them all.
@admin.route('/member/set_admin/<int:id>', methods=['GET', 'POST'])
def set_admin(id):
"""






# Rendering the page which contains the forms to be filled with information here.
@aicos_members.route('admin/cooperative/members/sendsms')
def sendsms():
    return render_template("employees/sendsms.html", title="Send SMS")



# Rendering the page which contains the forms to be filled with information here.
@aicos_members.route('/sendemail')
def sendemail():
    return render_template("employees/sendemail.html", title="Send SMS")




# Views for cooperatives subscription plans
@aicos_members.route('/department/subscription', methods=['GET', 'POST'])
@login_required
def subscriptions():
    check_admin()
    form = SubscriptionPlan()
    if form.validate_on_submit():
        subs = Subscription(subscribe_for=form.subscribe_for.data,
                            description=form.description.data,
                            subscription_plan=form.subscription_plan.data,
                            subscription_date=form.subscription_date.data,
                            credit_card_no   =form.credit_card_no.data)
        try:
            db.session.add(subs)
            db.session.commit()
            flash("Thank you for subscribing for this plan")
        except:
            flash("Your subscription has failed, please provide correct information")
        return redirect(url_for("aicos_members.list_departments"))
    return render_template("departments/subscriptions.html", form=form, title="Subscription")





@aicos_members.route('/cooperative/members/sendRemainder', methods=['GET', 'POST'])
@login_required
def sendRemainder():
    """
    List all employees
    """
    check_admin()
    check_coop_admin()
    #form = LoginForm()
    # if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)
    return render_template('employees/sendRemainder.html', title='Send Remainder')

    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')


@aicos_members.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('settings.html', title="Settings")



@aicos_members.route('/blank_page', methods=['GET', 'POST'])
def blank():
    return render_template('tools/blank.html', title="Blank Page")









# Views for the full details of a specific employee
@aicos_members.route('/cooperative_details', methods=['GET', 'POST'])
@login_required
def coop_details(email):
    #check_admin()

    #check_overall()
    #check_coop_admin()
    departments = Department.query.filter_by(email=current_user.email)




    employees = departments.members
    employees_count = departments.members.count()
    employees_male = departments.members.filter_by(gender='Gabo')
    employees_male_count = departments.members.filter_by(gender='Gabo').count()
    employees_female = departments.members.filter_by(gender='Gole')
    employees_female_count = departments.members.filter_by(gender='Gole').count()
    employees_abatarize = departments.members.filter_by(Amashuri='Abatarize')
    employees_abatarize_count = departments.members.filter_by(Amashuri='Abatarize').count()
    employees_abanza = departments.members.filter_by(Amashuri='Abanza')
    employees_abanza_count = departments.members.filter_by(Amashuri='Abanza').count()
    employees_ayisumbuye = departments.members.filter_by(Amashuri='Ayisumbuye')
    employees_ayisumbuye_count = departments.members.filter_by(Amashuri='Ayisumbuye').count()
    employees_kaminuza = departments.members.filter_by(Amashuri='Kaminuza')
    employees_kaminuza_count = departments.members.filter_by(Amashuri='Kaminuza').count()
    employees_imyuga = departments.members.filter_by(Amashuri='Imyuga')
    employees_imyuga_count = departments.members.filter_by(Amashuri='Imyuga').count()


    employees_amaguru = departments.members.filter_by(Ubumuga='Amaguru')
    employees_amaguru_count = departments.members.filter_by(Ubumuga='Amaguru').count()

    employees_amaboko = departments.members.filter_by(Ubumuga='Amaboko')
    employees_amaboko_count = departments.members.filter_by(Ubumuga='Amaboko').count()


    employees_kutabona = departments.members.filter_by(Ubumuga='Kutabona')
    employees_kutabona_count = departments.members.filter_by(Ubumuga='Kutabona').count()

    employees_kutumva = departments.members.filter_by(Ubumuga='Kutumva')
    employees_kutumva_count = departments.members.filter_by(Ubumuga='Kutumva').count()


    employees_mumutwe = departments.members.filter_by(Ubumuga='Mu mutwe')
    employees_mumutwe_count = departments.members.filter_by(Ubumuga='Mu mutwe').count()


    male_members = departments.members.filter_by(gender='Gole').first()
    if departments is not None:
        return render_template("cooperative_detail.html", departments=departments, 
                    employees=employees,
                             employees_count=employees_count,
                             male_members=male_members,
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
                    title="Cooperative's details")
    return redirect(url_for('admin.list_employees'))
