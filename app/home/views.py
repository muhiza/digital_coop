from flask import abort, render_template, request, redirect, flash, url_for
from flask_login import current_user, login_required
import stripe
from ..models import *
from . import home
from .forms import *
from .forms import newDepartmentForm


from .. import auth
from .. auth .forms import LoginForm, RegistrationForm
#from .. import db
from ..models import Employee

from markupsafe import Markup

import nexmo

client = nexmo.Client(key='e88f8d53', secret='w7j2m7zksG7RPPVc')


pub_key = "pk_test_l8INkseWioNZqSRgs78wq7AG"
secret_key = "sk_test_OXZNLFLMjrg0Lc2mSnp5htQw"
stripe.api_key = secret_key




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



@home.route('/')
def homepage():

    """
    Render the homepage template on the / route
    """
    return redirect(url_for('auth.login'))
    #return render_template('auth/landing_page.html', title="Welcome", pub_key=pub_key)



"""
Processing the payment logics
"""


@home.route('/allSolutions')
def allSolutions():
    return render_template('home/allSolutions.html')

    
@home.route('/pay', methods=['POST'])
def pay():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount   = 19900,
        currency = 'usd',
        description = 'The product'
        )
    
    flash("You have ordered a product from our store")
    return redirect(url_for('home.homepage'))



@home.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():

    employee = Employee.query.filter_by(username=current_user.username).first()
    employees = employee.department_id

    all_employees = Employee.query.filter_by(district=current_user.district)
    #all_employees      = employees_district.district

    all_cooperatives = Department.query.filter_by(district=current_user.district)

    if employee is not None:
        return render_template('home/dashboard.html', title="Dashboard", employee=employee, all_employees=all_employees, all_cooperatives=all_cooperatives)
    return render_template('home/dashboard.html', title="Dashboard", pub_key=pub_key, all_employees=all_employees, all_cooperatives=all_cooperatives)

    #return render_template('auth/login.html', form=form, title='Login')


@home.route('/products')
@login_required
def products():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/products.html', title="Products")


"""
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    departments = Department.query.filter_by(name='Marketing.')
    return render_template('home/admin_dashboard.html', title="Dashboard", departments = departments)
"""



# Employee Views
@home.route('/admin/cooperative', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    """
    List all employees
    """
    check_admin()
    #check_coop_admin()
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
    return render_template('home/admin_dashboard.html', employees=employees, applications=applications, apps=apps,
                           employee=employee, title='Employees')

    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')


# Employee Views
@home.route('/admin/dashboard/cooperative', methods=['GET', 'POST'])
@login_required
def admin_home_dashboard():
    """
    List all employees
    """
    check_admin()
    #check_coop_admin()
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
    return render_template('home/admin_home_dashboard.html', employees=employees, applications=applications, apps=apps,
                           employee=employee, title='Employees')


@home.route('/member/cooperatieve/join')
@login_required
def join_cooperative():
    all_cooperatives = Department.query.all()
    return render_template("home/all_cooperatives.html", title="Join Cooperative",
                           all_cooperatives=all_cooperatives)





page_num = 1
@home.route('/member/cooperatieve/search/<int:page_num>', methods=['GET', 'POST'])
@login_required
def search_coop(page_num):
    all_cooperatives = Department.query.paginate(per_page=6, page=page_num, error_out=True)
    return render_template("home/search_coop.html", title="Join Cooperative",
                           all_cooperatives=all_cooperatives)




@home.route('/admin/coops/quickSearch')
@login_required
def table_search():
    #check_admin()
    #check_overall()
    #check_coop_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Employee.query.count()

    all_depts_kigali = Department.query.filter_by(province='Kigali City').count()
    all_depts_west = Department.query.filter_by(province='West').count()
    all_depts_north = Department.query.filter_by(province='North').count()
    all_depts_south = Department.query.filter_by(province='South').count()
    all_depts_east = Department.query.filter_by(province='East').count()


    return render_template("home/table_search.html", employees=employees, 
                            departments=departments, all_mbs=all_mbs, all_depts=all_depts, 
                            all_depts_kigali=all_depts_kigali,
                            all_depts_south = all_depts_south,
                            all_depts_north = all_depts_north,
                            all_depts_east = all_depts_east,
                            all_depts_west = all_depts_west,
                            title="Dashboard Overall")



@home.route('/member/cooperatieve/done')
@login_required
def done():
    #all_cooperatives = Department.query.filter_by(is_active=0)
    return render_template("done.html", title="Join Cooperative")





@home.route('/cooperativeInfo/edit/<string:email>', methods=['GET', 'POST'])
@login_required
def coopInfo(email):
    """
    Edit a role
    """
    check_admin()
    #add_role = False
    coop = Department.query.get_or_404(email)
    form = DepartmentForm(obj=coop)
    if form.validate_on_submit():
        #coop.Code = form.Code.data
        coop.Name = form.Name.data
        coop.regdate = form.RegDate.data
        coop.Certificate = form.Certificate.data
        coop.Province   = form.Province.data
        coop.District   = form.District.data
        coop.Sector     = form.Sector.data
        coop.Cell       = form.Cell.data
        coop.startingShare = form.startingShare.data
        coop.Field         = form.Field.data
        coop.Description   = form.Description.data
        coop.email         = current_user.email
        coop.is_active         = 1
        code               = form.Code.data
        current_user.is_coop_admin = True
        current_user.department_id = current_user.email
        if form.Code.data == coop.code:        
            db.session.add(coop)
            db.session.commit()
            #flash('Umaze kwinjiza Cooperative yawe neza.')
            flash(Markup('Umaze kwinjiza Cooperative yawe neza., <b>Ongera winjire muri konti yawe!.</b>'), 'success')
            return redirect(url_for('home.done'))
        else:
            #flash('Code urimo kwinjiza ntago ihuye na Cooperative, Reba muri telephone yawe!.')
            #flash(Markup('Flashed message with <b>bold</b> statements'), 'success')
            flash(Markup('Code urimo kwinjiza ntago ihuye na Cooperative, <b>Wemerewe kwinjiza Code inshuro imwe!.</b>'), 'danger')
            to_number = '250780400612'
            message = 'Code ya cooperative ' + coop.Name + ' ku rubuga AICOS ni ' + coop.code
            response = client.send_message({'from' : '+250782061714', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

        # redirect to the roles page
        return redirect(url_for('home.coopInfo', email=email))


    #form.Code.data = coop.code
    form.Name.data = coop.name
    form.RegDate.data = coop.regdate
    form.Certificate.data = coop.certificate
    form.Province.data = coop.province
    form.District.data = coop.district
    form.Sector.data = coop.sector
    form.Cell.data = coop.cell
    form.startingShare.data = coop.starting_share
    #form.Field.data = coop.Field
    form.Description.data = coop.description
    return render_template('home/coop_info.html',
                           form=form, title="Edit Role")










@home.route('/cooperativeInfo/newApplication', methods=['GET', 'POST'])
@login_required
def newApplication():
    """
    Edit a role
    """
    check_admin()
    #add_role = False
    form = newDepartmentForm()
    if form.validate_on_submit():

        #coop.Code = form.Code.data
        newCoop = Department(
                        name = form.Name.data,
                        province   = form.Province.data,
                        district   = form.District.data,
                        sector     = form.Sector.data,
                        cell       = form.Cell.data,
                        starting_share = form.startingSharex.data,
                        share_per_person = form.sharePerPerson.data,
                        male_members         = form.maleMembers.data,
                        female_members         = form.femaleMembers.data,
                        is_active         = 1,
                        #current_user.is_coop_admin     = 1,
                        email         = current_user.email
                        #current_user.is_admin = 1
                    )

        try:      
            db.session.add(newCoop)
            current_user.is_coop_admin     = 1
            db.session.commit()
            #flash('Umaze kwinjiza Cooperative yawe neza.')
            flash(Markup('Umaze kwinjiza Cooperative yawe neza., <b>Ongera winjire muri konti yawe!.</b>'), 'success')
            return redirect(url_for('home.done'))
        except:
            #flash('Code urimo kwinjiza ntago ihuye na Cooperative, Reba muri telephone yawe!.')
            #flash(Markup('Flashed message with <b>bold</b> statements'), 'success')
            flash(Markup('Umwirondoro wa Koperative urimo gushyiramo ntago wuzuye, <b>Ongera ugerageze!.</b>'), 'danger')
            to_number = '250780400612'
            message = 'Code ya cooperative ku rubuga AICOS ni '
            response = client.send_message({'from' : '+250782061714', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]

        # redirect to the roles page
        return redirect(url_for('home.done'))




    return render_template('home/new_coop.html',
                           form=form, title="Edit Role")











@home.route('/cooeprativeCode/sendCode')
def sendCode():
    flash("Code ya Cooperative yoherejwe kuri telephone yawe!")
    return redirect(url_for('home.done'))


























































@home.route('/application/sent')
def thankyou():
    return render_template("home/thankyou.html", title="Thank you!")





@home.route('/members/cooperatieve/<string:email>/details')
@login_required
def cooperative_details(email):
    cooperative = Department.query.get_or_404(email)
    employees = Profile.query.all()
    return render_template("home/cooperative_details.html", title="Cooperative details", cooperative=cooperative, employees=employees)



@home.route('/cooperatives/categories')
def coop_categories():
    coop_categories = Department.query.filter_by(category="Education")
    return render_template("home/cooperatives_categories.html", title="Cooperatives Categories", coop_categories=coop_categories)



#Views for the profile of the normal user of the system.
@home.route('/user/<int:id>/profile/<string:username>')
@login_required
def user_profile(id, username):

    #check_admin()

    user = Employee.query.filter_by(email=current_user.email).first()
    department = Department.query.filter_by(email=user.department_id).first()

    return render_template("home/user_profile.html", title="User profile", user=user, department = department)




#Views for the profile of the normal user of the system.
@home.route('/user/<int:id>/profile/<string:username>/accept')
@login_required
def accept(id, username):

    #check_admin()

    user = Employee.query.filter_by(email=current_user.email).first()
    #department = Department.query.filter_by(email=user.department_id).first()

    user.department_id = user.invited_by
    db.session.commit()
    user.invited_by = None
    db.session.commit()
    flash("You joined cooperative successfully")
    #return redirect(url_for("home.user_profile"))
    return render_template("home/user_profile.html", title="User profile", user=user)



# Processing the application form of the members
@home.route('/member/application', methods=['GET', 'POST'])
@login_required
def application():

    #department = Department.query.get_or_404(email)
    #form = DepartmentForm(obj=department)
    #cooperative = Department.query.all()


    form = ApplicationForm()

    if form.validate_on_submit():

        applicant = Application(
                                emailaa = form.Emaila.data,
                                firstNameaa = form.firstNamea.data,
                                secondNameaa = form.secondNamea.data,
                                othersaa     = form.othersa.data,
                                Districtaa  = form.Districta.data,
                                Sectoraa  = form.Sectora.data,
                                Cellaa = form.Cella.data,
                                nIdaa = form.nIda.data,
                                entryDateaa = form.entryDatea.data,
                                shareaa     = form.sharea.data,
                                exitDateaa     = form.exitDatea.data,
                                umuzunguraaa     = form.umuzunguraa.data,
                                umukonoaa     = form.umukonoa.data,
                                genderaa = form.gendera.data,
                                dobaa    = form.doba.data,
                                phoneaa  = form.phonea.data,
                                Amashuriaa  = form.amashuria.data,
                                Ubumugaaa  = form.ubumugaa.data,
                                department_id = "123"

                                )
        try:
            db.session.add(applicant)
            db.session.commit()
            flash("You application has been submited successfully")
        except:
            flash("There is an error in your application")
        return redirect(url_for("home.thankyou"))

    return render_template("home/application.html", form=form, title="Membership Application Form")








@home.route('/user/<int:id>/profile/about', methods=['GET', 'POST'])
def user_profile_about(id):
    form = ProfileForm()
    if form.validate_on_submit():
        user_profile = Profile(primary_school=form.primary_school.data,
                               secondary_school=form.secondary_school.data,
                               university_school=form.university_school.data,
                               vocational_school=form.vocational_school.data,
                               exp1             = form.exp1.data,
                               exp2             = form.exp2.data,
                               exp3             = form.exp3.data,
                               strn1            = form.strn1.data,
                               strn2            = form.strn2.data,
                               strn3            = form.strn3.data,
                               car1            = form.car1.data,
                               car2            = form.car2.data,
                               car3            = form.car3.data,
                               district        = form.district.data,
                               inter1          = form.inter1.data,
                               inter2          = form.inter2.data,
                               inter3          = form.inter3.data

                               )

        try:
            db.session.add(user_profile)
            db.session.commit()
            flash("You have updated your profile successfully")
        except:
            flash("The is an error in your form, please correct it and submit again")
        return redirect(url_for('home.user_profile', id=current_user.id, username=current_user.username))
    return render_template("home/user_profile_about.html", title="Tell us about you", form=form)











