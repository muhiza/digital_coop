from flask import abort,  request, flash, redirect, render_template, url_for, jsonify
from flask_login import current_user, login_required
from . import admin
from .forms import *
#from forms import DepartmentForm, EmployeeAssignForm, RoleForm, SendSMS, 
#ProjectForm, ClientForm, ProductForm, NewEmployee, SubscriptionPlan, ProductForm, OrderForm
from .. auth.forms import *
from .. models import *
from .. import db, api
#from ..models import Department, Employee, Role, Project, Client, Subscription, Post, Category, Product, Decision
from ..models import * 
import nexmo
from flask import Flask, request, jsonify
import flask_excel as excel
from sqlalchemy import func
# Api test related imports
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import make_response
import pdfkit
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

# Department Views
@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()
    #patients = Patient.query.filter(Patient.mother.has(phenoscore=10))
    #form = LoginForm()
    #if form.validate_on_submit():
    #check whether employee exists in the database and whether
    #the password entered matches the password in the database
    departments = Department.query.filter_by(email=current_user.email).first()
    #if departments is not None:
    #employees = Employee.query.filter_by(email=form.email.data)
    return render_template('admin/departments/departments.html', departments=departments, title="Your Cooperative")
    #employee = Employee.query.filter_by(email=form.email.data).first()
    #departments = Department.query.all()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    # departmentsz = Department.query.filter_by(email='muhiza@gmail.com').first()
    # departments  = departmentsz.employees.filter_by(email=form.email.data).first()
    #return render_template('auth/login.html', form=form, title='Login')

@admin.route('/departments/add', methods=['POST', 'GET'])
@login_required
def add_department():
    """
    Add a cooperative to the database,
    here we are to consider two difference things when adding a cooperative,

    1 : There are those cooperaves which are already registred with RCA
        what a user will do is to prove that is is belong to that cooperative and then be allowed to join it.

    2 : This option is where the user will come and register and after registering they will register new cooperatives
        from scratch according to the law of coop registration and then they be able to access and use all other services.
    """
    #check_admin()
    add_department = True
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(code=form.Code.data,
                                name=form.Name.data,
                                regdate=form.RegDate.data,
                                certificate=form.Certificate.data,
                                province=form.Province.data,
                                district=form.District.data,
                                sector=form.Sector.data,
                                field=form.Field.data,
                                activity=form.Activity.data,
                                starting_share=form.startingShare.data,
                                email=current_user.email,
                                description=form.Description.data)
        try:
            # add department to the database
            #coop = Department.query.filter_by(email='urunana@gmail.com').first()
            coop_admin = Employee.query.filter_by(email=current_user.email).first()
            #coop_admin.department_id = 'urunana@gmail.com'
            coop_admin.is_coop_admin = True
            coop_admin.is_admin = True
            coop_admin.department_id = current_user.email
            db.session.add(department)
            db.session.commit()
            #db.session.add(department)
            #coop_admin = Employee.query.filter_by(email=current_user.email).first()
            #coop_admin.department_id = current_user.email
            #db.session.commit()
            flash('You have successfully created a cooperative.')
        except:
            # in case department name already exists
            flash(' Error: The cooperative ' + str(department.name) + ' does not exist, please try again')
        # redirect to departments page
        return redirect(url_for('aicos_members.cooper_details'))
    # load department template
    return render_template('admin/departments/department.html', action="Add", add_department=add_department, form=form, title="Create Cooperative")

@admin.route('/join_Cooperative_Code/edit/<int:no>', methods=['GET', 'POST'])
@login_required
def join_cooperative_code(no):
    """
    Edit a role
    """
    #check_admin()
    #add_role = False
    role = Department.query.get_or_404(no)
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

@admin.route('/departments/edit/', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()
    add_department = False
    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.email = form.email.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')
        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))
    form.description.data = department.description
    form.email.data = department.email
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")

@admin.route('/departments/delete/', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')
    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))
    return render_template(title="Delete Department")

# The view to set one member of the cooperative as the cooperative member from other members and them manage them all.
@admin.route('/member/set_admin/<int:id>', methods=['GET', 'POST'])
def set_memb_as_admin(id):
    check_admin()
    check_coop_admin()
    employeee = Employee.query.get_or_404(id)
    employeee.is_coop_admin = True
    #employeee.email = current_user.email
    db.session.commit()
    flash("You have set " + str(employeee.username) + " as cooperative admin")
    return redirect(url_for('admin.list_employees'))

@admin.route('admin/cooperative/all_exports')
def allexports():
    return render_template("admin/tools/pdf/export.html", title="Send SMS")

# This is the class which will be used to Send some sms.
@admin.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    #form  = SendSMS()
    #check_admin()
        # Extract the form values:
    to_number = request.form['to_number']
    message = request.form['message']
    response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
    response_text = response['messages'][0]
    return redirect(url_for('admin.sendsms'))
    #return render_template("admin/employees/sendsms.html", title="Send SMS")

# This is the class which will be used to Send some sms.
@admin.route('/sendmail', methods=['GET', 'POST'])
@login_required
def sendmail():
    #form  = SendSMS()
    #check_admin()
        # Extract the form values:
    to_number = request.form['to_number']
    message = request.form['message']
    response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
    response_text = response['messages'][0]
    return redirect(url_for('admin.sendemail'))
    #return render_template("admin/employees/sendsms.html", title="Send SMS")
    """
    Projects side views and all operations related to the project table.
    """
@admin.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():
    check_admin()
    projects = Project.query.all()
    return render_template("admin/projects/projects.html", projects = projects, title = "Projects")

@admin.route('/project/add', methods=['GET', 'POST'])
@login_required
def add_project():
    check_admin()
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data,
                          description=form.description.data,
                          duration=form.description.data)
        try:
            db.session.add(project)
            db.session.commit()
            flash("The project has been added successfuly")
        except:
            flash("Error: This project is registered")
        return redirect(url_for("admin.projects"))
    return render_template("admin/projects/project.html", form =form, title="Project")

@admin.route('/admin/recent_activities/report')
@login_required
def recent_activities():
    #check_admin()
    #check_coop_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Member.query.count()
    notes = Department.query.filter_by(email=current_user.email).first()
    notifications = notes.notifications

    date = datetime.datetime.now()
    rendered = render_template('admin/tools/pdf/recent_activities.html',
        notifications=notifications, date=date)
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response
    return render_template("admin/tools/pdf/recent_activities.html", notifications=notifications, 
                            employees=employees, departments=departments, all_mbs=all_mbs, all_depts=all_depts, 
                            title="Dashboard Coop Admin")

@admin.route('/admin/dashboard_user')
@login_required
def dashboard_user():
    check_admin()
    check_overall()
    check_coop_admin()
    employees = Member.qdecuery.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Member.query.count()
    notifications = Notification.query.all()
    return render_template("admin/user/dashboard_user.html", employees=employees, notifications=notifications, 
                            departments=departments, all_mbs=all_mbs, all_depts=all_depts, title="Dashboard Overall")

@admin.route('/admin/overall')
@login_required
def overall():
    check_admin()
    check_overall()
    employees = Member.query.all()
    departments = Department.query.all()
    return render_template("admin/overall/all.html", employees=employees, departments=departments, 
                            title="Overall dashboard")

@admin.route('/admin/overall_members')
@login_required
def overall_members():
    check_admin()
    check_overall()
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template("admin/overall/overall_members.html", employees=employees, departments=departments, 
                            title="Overall dashboard")

"""
# View to deal with excel file upload handling.
#@amdin.
SQLALCHEMY_DATABASE_URI = 'mysql://root:annemuhiza@localhost/smartest'
@admin.route("/import", methods=['GET', 'POST'])
def doimport():
    if request.method == 'POST':
        def role_init_func(row):
            r = Role(row['name'])
            r.description = row['description']
            r.id = row['id']
            return r
        request.save_book_to_database(
            field_name='file', session=db.session,
            tables=[Role],
            initializers=[role_init_func])
        #return redirect(url_for('.handson_table'), code=302)
        flash("You have uploaded excel file successfully")
        return redirect(url_for('admin.list_departments'), code=302)
    return render_template("admin/employees/upload.html", title="Upload a file")
"""

# This is the view used to import all the cooperatives from excel sheet.
SQLALCHEMY_DATABASE_URI = 'mysql://root:annemuhiza@localhost/coop'
@admin.route("/importcoops", methods=['GET', 'POST'])
def doimportcoops():
    if request.method == 'POST':
        def coop_init_func(row):
            c = Department(row['id'])
            c.id = row['id']
            c.no = row['no']
            c.code = row['code']
            #c.email = row['email']
            c.name = row['name']
            c.regdate = row['regdate']
            c.certificate = row['certificate']
            c.description = row['description']
            c.province = row['province']
            c.district = row['district']
            c.sector = row['sector']
            c.activity = row['activity']
            c.coop_type = row['coop_type']
            c.category = row['category']
            c.field = row['field']
            c.started_date = row['started_date']
            c.starting_share = row['starting_share']
            c.cell = row['cell']
            c.is_active = row['is_active']
            #c.id = row['id']
            return c
        request.save_book_to_database(
            field_name='file', session=db.session,
            tables=[Department],
            initializers=[coop_init_func])
        #return redirect(url_for('.handson_table'), code=302)
        flash("You have uploaded excel file successfully")
        return redirect(url_for('admin.doimportcoops'), code=302)
    return render_template("admin/upload.html", title="Upload a file")

# This is the view used to import all the unions from excel sheet.
SQLALCHEMY_DATABASE_URI = 'mysql://root:annemuhiza@localhost/coop'
@admin.route("/importunions", methods=['GET', 'POST'])
def doimportunions():
    if request.method == 'POST':
        def union_init_func(row):
            c = Union(row['id'])
            c.id = row['id']
            c.no = row['no']
            c.code = row['code']
            #c.email = row['email']
            c.name = row['name']
            c.regdate = row['regdate']
            c.certificate = row['certificate']
            c.province = row['province']
            c.district = row['district']
            c.sector = row['sector']
            c.activity = row['activity']
            #c.id = row['id']
            return c
        request.save_book_to_database(
            field_name='file', session=db.session,
            tables=[Union],
            initializers=[union_init_func])
        #return redirect(url_for('.handson_table'), code=302)
        flash("You have uploaded excel file successfully")
        return redirect(url_for('admin.doimportunions'), code=302)
    return render_template("admin/uploadunions.html", title="Upload a file")

# This is the view used to import all the unions from excel sheet.
SQLALCHEMY_DATABASE_URI = 'mysql://root:annemuhiza@localhost/coop'
@admin.route("/importfed", methods=['GET', 'POST'])
def doimportfed():
    if request.method == 'POST':
        def fed_init_func(row):
            c = Federation(row['id'])
            c.id = row['id']
            c.no = row['no']
            c.code = row['code']
            #c.email = row['email']
            c.name = row['name']
            c.reg_date = row['regdate']
            c.certificate = row['certificate']
            c.province = row['province']
            c.district = row['district']
            c.sector = row['sector']
            c.activity = row['activity']
            #c.id = row['id']
            return c
        request.save_book_to_database(
            field_name='file', session=db.session,
            tables=[Federation],
            initializers=[fed_init_func])
        #return redirect(url_for('.handson_table'), code=302)
        flash("You have uploaded excel file successfully")
        return redirect(url_for('admin.doimportfed'), code=302)
    return render_template("admin/uploadfed.html", title="Upload a file")
    """
    #Importing excel sheet for the cooperatives.
    @admin.route("/import", methods=['GET', 'POST'])
    def doimport():
        if request.method == 'POST':


            #def category_init_func(row):
                #c = Category(row['name'])
                #c.id = row['id']
                #return c

            def coop_init_func(row):
                #c = Category.query.filter_by(name=row['category']).first()
                p = Department(row['no'], row['code'], row['name'], row['certificate'], row['regdate'], row['province'], row['district'], row['sector'], row['activity'])
                return p


            #def post_init_func(row):
                #c = Category.query.filter_by(name=row['category']).first()
                #p = Post(row['title'], row['body'], c, row['pub_date'])
                #return p
                
            request.save_book_to_database(
                field_name='file', session=db.session,
                tables=[Department, Employee],
                initializers=[coop_init_func])
            flash("You have uploaded excel file successfully")
            return redirect(url_for('admin.list_departments'), code=302)
        return render_template("admin/employees/upload.html", title="Upload a file")
    """
# Views for business solutions.
@admin.route('/business/solutions')
@login_required
def solutions_list():
    check_admin()
    return render_template("solutions/inventory/home/index.html", title="Business solutions")

# Views for business solutions.
@admin.route('/cooperative/proof')
@login_required
def proof():
    check_admin()
    dept = Department.query.filter_by(email=current_user.email).first()
    products = dept.products
    orders = dept.orders
    return render_template("solutions/inventory/proof.html", dept=dept, products=products, orders=orders, title="Business solutions")

# View to deal with the product registrations.
@admin.route('/cooperative/proof/product', methods=['GET', 'POST'])
@login_required
def add_product():
    check_admin()
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name       =form.name.data,
                          description=form.description.data,
                          quantity   = form.quantity.data,
                          in_date    = form.in_date.data,
                          status     = form.status.data,
                          department_id = current_user.email)
        db.session.add(product)
        db.session.commit()
        flash("You have successully added new product in the inventory")
        return redirect(url_for('admin.proof'))
    return render_template("solutions/inventory/products.html", form=form)

#View to deal with the orders registrations.
@admin.route('/cooperative/proof/orders', methods=['GET', 'POST'])
@login_required
def add_order():
    check_admin()
    form = OrderForm()
    if form.validate_on_submit():
        order     = Order(name       =form.name.data,
                          product    = form.product.data,
                          description=form.description.data,
                          quantity   = form.quantity.data,
                          in_date    = form.in_date.data,
                          status     = form.status.data,
                          department_id = current_user.email)
        db.session.add(order)
        db.session.commit()
        flash("You have successully added new order in the inventory")
        return redirect(url_for('admin.proof'))
    return render_template("solutions/inventory/new_order.html", form=form, title="New order")

# Views for business solutions.
@admin.route('/cooperative/products')
@login_required
def product_list():
    check_admin()
    dept = Department.query.filter_by(email=current_user.email).first()
    products = dept.products
    orders = dept.orders
    return render_template("solutions/inventory/product_list.html", dept=dept, 
                            products=products, orders=orders, title="All products")

@admin.route('/api/v10')
@login_required
def product_api():
    check_admin()
    dept = Department.query.filter_by(email=current_user.email).first()
    if not dept:
        abort(404)
    res = {
        'name': dept.name,
        'id': str(dept.email),
    }
    return jsonify(res)
# Dealing with all activities that concerns admin block
# In the later varsion this and other stuffs related to admin
# Will be moved to the admin's special blueprint and leave this blueprint
# for the overall user.
@admin.route('/cooperative/create')
@login_required
def create():
    check_admin()
    check_coop_admin()
    return render_template("admin/tools/create.html", title="Create")
"""
@admin.route('/cooperative/create/decision')
@login_required
def create_decision():
    check_admin()
    check_coop_admin()
    return render_template("admin/tools/create.html", title="Create")

@admin.route('/cooperative/create/how_to_article')
@login_required
def create_how_to_article():
    check_admin()
    check_coop_admin()
    return render_template("admin/tools/create.html", title="Create")

@admin.route('/cooperative/create/meeting_notes')
@login_required
def create_meeting_notes():
    check_admin()
    check_coop_admin()
    return render_template("admin/tools/create.html", title="Create")

@admin.route('/cooperative/create/retrospective')
@login_required
def create_retrospective():
    check_admin()
    check_coop_admin()
    return render_template("admin/tools/create.html", title="Create")

@admin.route('/cooperative/create/meeting_notes')
@login_required
def create_meeting_notes():
    check_admin()
    check_coop_admin()
    return render_template("admin/tools/create.html", title="Create")

@admin.route('/cooperative/create/retrospective')
@login_required
def create_retrospective():
    check_admin()
    check_coop_admin()
    return render_template("admin/tools/create.html", title="Create")
"""

@admin.route('/admin/fin_dashboard')
@login_required
def fin_dashboard():
    #check_admin()
    #check_coop_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Member.query.count()
    notifications = Notification.query.all()
    return render_template("admin/coop/fin/fin_dashboard.html", employees=employees, 
                            notifications=notifications, departments=departments, all_mbs=all_mbs, 
                            all_depts=all_depts, title="Dashboard Coop Admin")

@admin.route('/admin/ezigama')
@login_required
def ezigama():
    #check_admin()
    #check_coop_admin()
    employees = Member.query.all()
    departments = Department.query.all()
    all_depts = Department.query.count()
    all_mbs = Member.query.count()
    notifications = Notification.query.all()

    return render_template("admin/coop/fin/ezigama.html", employees=employees, 
        notifications=notifications, departments=departments, all_mbs=all_mbs, 
        all_depts=all_depts, title="Dashboard Coop Admin")
# Adding a member in a coop
"""
"""
@admin.route('/cooperative/create/member_bank_account', methods=['GET', 'POST'])
@login_required
def addBankAccount():
    check_admin()
    form = bankAccountForm()
    if form.validate_on_submit():
        newBankAccount = BankAccount(memberId=form.memberId.data,
                        memberName=form.memberName.data,
                        bankAccountNumber   = form.bankAccountNumber.data,
                        accountType=form.accountType.data,
                        amount=form.amount.data,
                        date = form.date.data,
                        department_id = current_user.email
                        )
        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "12-12-2017",
                            done_to="Muhiza",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(newBankAccount)
            db.session.add(notif)
            db.session.commit()
            to_number = '+250786012383'
            message = current_user.email + 'New member has been created in the cooperatives'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            flash("You have successfully created a new member")
        except:
            flash("Error! Invalid information was given")
        return redirect(url_for('admin.decisions_list'))
    return render_template("admin/employees/newBankAccount.html", form=form, title="Add New Bank Account")

#All members and their financial related details.
@admin.route('/cooperative/members_financials', methods=['GET', 'POST'])
@login_required
def list_members_financials():
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
    return render_template('admin/employees/membersFinancials.html',
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
@admin.route('/member_financial_details/<int:id>', methods=['GET', 'POST'])
@login_required
def member_financial_details(id):
    check_admin()
    employee = Member.query.get_or_404(id)
    if employee is not None:
        return render_template("admin/employees/memberFinancialDetails.html", employee=employee)
    return redirect(url_for('admin.list_employees'))

# Member's Loan Application Form.
@admin.route('/cooperative/member/loanApplication', methods=['GET', 'POST'])
@login_required
def applyLoan():
    check_admin()
    form = LoanForm()
    if form.validate_on_submit():
        new_loan = Loan(    memberId=form.memberId.data,
                        memberName=form.memberName.data,
                        introducer1Id   = form.introducer1Id.data,
                        introducer1Name=form.introducer1Name.data,
                        introducer1BankAccountBalance=form.introducer1BankAccountBalance.data,
                        introducer1Share = form.introducer1Share.data,

                        introducer2Id = form.introducer2Id.data,
                        introducer2Name = form.introducer2Name.data,
                        introducer2BankAccountBalance = form.introducer2BankAccountBalance.data,
                        introducer2Share = form.introducer2Share.data,

                        loanAmount = form.loanAmount.data,
                        interestRate = form.interestRate.data,
                        durationInDay  = form.durationInDay.data,
                        remarksIfAny = form.remarksIfAny.data,
                        loanType = form.loanType.data,
                        totalLoanWithInterest = form.totalLoanWithInterest.data,
                        activedBy = form.activedBy.data,
                        loanIssueDate = form.loanIssueDate.data
                        )
        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "12-12-2017",
                            done_to="Muhiza",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(new_loan)
            db.session.add(notif)
            db.session.commit()
            to_number = '+250786012383'
            message = current_user.email + 'New member has been created in the cooperatives'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            flash("You have successfully applied for Loan")
        except:
            flash("Error! Invalid information was given")
        return redirect(url_for('admin.decisions_list'))
    return render_template("admin/employees/loan_form.html", form=form, title="Apply for Loan")
# View for adding fixed deposit account
@admin.route('/cooperative/member/add/fixedDepositAccount', methods=['GET', 'POST'])
@login_required
def fixedAcc():
    check_admin()
    form = fixedD()
    if form.validate_on_submit():
        fixedAcc = fixedDepositAccount(     memberId=form.memberId.data,
                                            memberName=form.memberName.data,
                                            fixedDepositAmount   = form.fixedDepositAmount.data,
                                            durationInDay=form.durationInDay.data,
                                            fixedDepositInterest=form.fixedDepositInterest.data,
                                            maturityDate = form.maturityDate.data,
                                            matureAmount = form.matureAmount.data,
                                            createdBy = form.createdBy.data,
                                            date = form.date.data
                                        )
        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "12-12-2017",
                            done_to="Muhiza",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(fixedAcc)
            db.session.add(notif)
            db.session.commit()
            to_number = '+250786012383'
            message = current_user.email + 'New member has been created in the cooperatives'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            flash("You have successfully created new Fixed Deposit Account")
        except:
            flash("Error! Invalid information was given")
        return redirect(url_for('admin.decisions_list'))
    return render_template("admin/employees/fixed_deposit_account_form.html", form=form, title="Apply for Loan")
# View for user's transactions
@admin.route('/cooperative/member/transactions', methods=['GET', 'POST'])
@login_required
def transactions():
    check_admin()
    form = transactionForm()
    if form.validate_on_submit():
        trans = Transaction(                bankAccountNumber=form.bankAccountNumber.data,
                                            memberName=form.memberName.data,
                                            accountType   = form.accountType.data,
                                            depositOrWithdraw=form.depositOrWithdraw.data,
                                            cashOrCheque=form.cashOrCheque.data,
                                            amount = form.amount.data,
                                            balance = form.balance.data,
                                            date = form.date.data
                                        )
        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "12-12-2017",
                            done_to="Muhiza",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(trans)
            db.session.add(notif)
            db.session.commit()
            to_number = '+250786012383'
            message = current_user.email + 'New member has been created in the cooperatives'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            flash("You have successfully made a transaction")
        except:
            flash("Error! Invalid information was given")
        return redirect(url_for('admin.decisions_list'))
    return render_template("admin/employees/transaction_form.html", form=form, title="Deposit or Withdraw money")

# View for users' shares 
@admin.route('/cooperative/member/shares', methods=['GET', 'POST'])
@login_required
def share():
    check_admin()
    form = shareForm()
    if form.validate_on_submit():
        newShare = Share(       memberId=form.memberId.data,
                                shareAccNo=form.shareAccNo.data,
                                memberName=form.memberName.data,
                                depositOrWithdraw=form.depositOrWithdraw.data,
                                shareAmount=form.shareAmount.data,
                                balanceShare = form.balanceShare.data,
                                date = form.date.data
                            )
        notif = Notification(action="Made decision",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "12-12-2017",
                            done_to="Muhiza",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(newShare)
            db.session.add(notif)
            db.session.commit()
            to_number = '+250786012383'
            message = current_user.email + 'New member shares has been created'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            flash("You have successfully deposited your shares")
        except:
            flash("Error! Invalid information was given")
        return redirect(url_for('admin.decisions_list'))
    return render_template("admin/employees/share_form.html", form=form, title="Deposit Shares")

# View for user's loan installment payment
@admin.route('/cooperative/member/installment', methods=['GET', 'POST'])
@login_required
def installment():
    check_admin()
    form = installmentForm()
    if form.validate_on_submit():
        install = Installment(   memberId=form.memberId.data,
                                loanId=form.loanId.data,
                                memberName=form.memberName.data,
                                lastInstallmentPay=form.lastInstallmentPay.data,
                                lastInstallmentPayDate=form.lastInstallmentPayDate.data,
                                cashOrCheque = form.cashOrCheque.data,
                                payLoanInstallment = form.payLoanInstallment.data,
                                balance = form.balance.data,
                                remarksIfAny = form.remarksIfAny.data,
                                date = form.date.data
                            )
        notif = Notification(action="Made loan Installment Payment",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "12-12-2017",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            db.session.add(install)
            db.session.add(notif)
            db.session.commit()
            to_number = '+250786012383'
            message = current_user.email + 'New loan Installment Payment has been made'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            flash("You have successfully made payment")
        except:
            flash("Error! Invalid information was given")
        return redirect(url_for('admin.decisions_list'))
    return render_template("admin/employees/installment_form.html", form=form, title="Installment Payment")

# All members and their financial related details.
@admin.route('/cooperative/members/saving_and_current_accounts', methods=['GET', 'POST'])
@login_required
def currentSavingAccount():
    """
    List all employees
    """
    check_admin()
    check_coop_admin()
    #form = LoginForm()
    # if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
    #apps = BankAccount.query.all()
    #all_bank_accounts = apps.applications
    others = Department.query.filter_by(email=current_user.email).first()
    all_bank_accounts = others.BankAccounts
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)
    return render_template('admin/employees/currentSavingAccount.html',
                           employees=employees,
                           employee=employee, all_bank_accounts=all_bank_accounts, title='Employees')
    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

# All members and their financial related details.
@admin.route('/cooperative/members/all_given_loans', methods=['GET', 'POST'])
@login_required
def givenLoans():
    """
    List all employees
    """
    check_admin()
    check_coop_admin()
    #form = LoginForm()
    # if form.validate_on_submit():
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
    loan = Department.query.filter_by(email=current_user.email).first()
    all_given_loans = loan.loans
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)
    return render_template('admin/employees/loans.html',
                           employees=employees,
                           employee=employee, all_given_loans=all_given_loans, title='All Given Loans')
    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

@admin.route('/cooperative/members/all_fd_account', methods=['GET', 'POST'])
@login_required
def fdAccount():
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
    return render_template('admin/employees/allFDaccount.html',
                           employees=employees, applications=applications, apps=apps,
                           employee=employee, title='All Fixed Deposit Account')
    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

@admin.route('/cooperative/members/share_account', methods=['GET', 'POST'])
@login_required
def shareAccount():
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
    return render_template('admin/employees/shareAccount.html',
                           employees=employees, applications=applications, apps=apps,
                           employee=employee, title='All Share Accounts')
    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')
@admin.route('/cooperative/members/memberIcard', methods=['GET', 'POST'])
@login_required
def memberIcard():
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
    return render_template('admin/employees/memberIcard.html', title='Member Icard')

    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

@admin.route('/cooperative/members/bankAccountStatement', methods=['GET', 'POST'])
@login_required
def bankAccountSat():
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
    return render_template('admin/employees/bankAccountStatement.html', title='Bank Account Statement')

    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

@admin.route('/cooperative/members/shareStatement', methods=['GET', 'POST'])
@login_required
def shareSat():
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
    return render_template('admin/employees/shareStatement.html', title='Share Statement')

    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

@admin.route('/cooperative/members/loanReceipt', methods=['GET', 'POST'])
@login_required
def loanReceipt():
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
    return render_template('admin/employees/loanReceipt.html', title='Loan Receipt')
    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')
@admin.route('/cooperative/members/fdCertificate', methods=['GET', 'POST'])
@login_required
def fdCertificate():
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
    return render_template('admin/employees/fdCertificate.html', title='FD Certificate')
    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

@admin.route('/cooperative/members/dueDurationSetup', methods=['GET', 'POST'])
@login_required
def dueDurationSetup():
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
    return render_template('admin/employees/dueDurationSetup.html', title='Due Duration Setup')
    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

@admin.route('/cooperative/members/cooperativeSetup', methods=['GET', 'POST'])
@login_required
def cooperativeSetup():
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
    return render_template('admin/employees/cooperativeSetup.html', title='Cooperative Setup')
    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

@admin.route('/cooperative/members/loanSetup', methods=['GET', 'POST'])
@login_required
def loanSetup():
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
    return render_template('admin/employees/loanSetup.html', title='Loan Setup')

    # departments = Department.query.filter_by(name='IT').first()
    # employees = departments.employees.filter_by(email=form.email.data).first()
    #departments = Employee.query.filter_by(email=form.email.data).first()
    #employees = Employee.query.all()
    # employees = Employee.query.all()
    #return render_template('auth/login.html', form=form, title='Login')
    #return render_template('admin/employees/employees.html',
                          # employees=employees, title='Employees')

class Depts(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        #query = conn.execute("select * from employees") # This line performs query and returns json result

        query = Department.query.all()
        return {'departments': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        #conn = db_connect.connect()
        #query = conn.execute("select trackid, name, composer, unitprice from tracks;")

        query = Employee.query.all()
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

"""
class Employees_Name(Resource):
    def get(self, department_email):
        #conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        """
api.add_resource(Depts, '/muhiza') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
from flask_restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('description', type=str)

@admin.route('/iwacunawe')
def home():
    return "Welcome to the Catalog Home, Muhiza Frank"

class RoleApi(Resource):
    def get(self, id=None, page=1):
        if not id:
            products = Role.query.paginate(page, 10).items
        else:
            products = [Role.query.get(id)]
        if not products:
            abort(404)
        res = {}
        for product in products:
            res[Role.id] = {
                'name': product.name,
                'description': product.description,
            }
        return json.dumps(res)
api.add_resource(RoleApi, '/hore')