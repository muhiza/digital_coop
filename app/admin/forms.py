from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, FileField, DateTimeField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email
#from ..models import Department, Role, Employee, Product
from ..models import *
from markupsafe import Markup
from flask_wtf.file import FileField, FileAllowed, FileRequired
from .. import images

class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    Code = StringField('Code ya Cooperative', validators=[DataRequired()], render_kw={"placeholder": "Injiza Code ya cooperative"})
    Name = StringField('Izina rya Cooperative', validators=[DataRequired()], render_kw={"placeholder": "Injiza izina rya Cooperative"})
    RegDate = StringField('Igihe Cooperative yandikiwe', validators=[DataRequired()], render_kw={"placeholder": "Injiza italiki yandikiweho"})
    Certificate = StringField('Certificate ya Cooperative', validators=[DataRequired()], render_kw={"placeholder": "Shyiramo certificate ya Cooperative"})
    Province = SelectField(
        'Intara Cooperative ibarizwamo',
        choices=[('Intara', 'Intara'),('Kigali City', 'Kigali City'), 
        ('East', 'East'), ('West', 'West'),
        ('North', 'North'), ('South', 'South')])
    District = SelectField(
        'Hitamo akarere Cooperative ibarizwamo',
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
    Sector = StringField('Injiza umurenge', validators=[DataRequired()], render_kw={"placeholder": "Injiza umurenge cooperative ibarizwamo"})
    Cell = StringField('Injiza akagari', validators=[DataRequired()], render_kw={"placeholder": "Injiza akagari Cooperative ibarizwamo"})
    startingShare = StringField('Umugabane Shingiro', validators=[DataRequired()], render_kw={"placeholder": "Umugabane Shingiro wo Kwinjira muri Cooperative"})
    Field = SelectField(
        'Hitamo umurimo Cooperative ikora',
        choices=[('Coop Sector', 'Coop Sector'),('Tea', 'Tea'), 
        ('Mining', 'Mining'), ('Dairy', 'Dairy'),
        ('Coffee', 'Coffee'), ('Cassava', 'Cassava'),
        ('Irish Potato', 'Irish Potato'), ('Motor Cycle Transport', 'Motor Cycle Transport'),
        ('Bee Keeping', 'Bee Keeping'), ('Wheat Growers', 'Wheat Growers'),
        ('Rice Growers', 'Rice Growers'), ('Minibus Transport', 'Minibus Transport'),
        ('Maize Growers', 'Maize Growers'), ('Fishing', 'Fishing'),
        ('Horticulture', 'Horticulture'), ('Fishing', 'Fishing')])
    Description = TextAreaField('Ubundi busobanuro bwa Cooperative', validators=[DataRequired()], render_kw={"placeholder": "Enter Comment or Descriptions"})
    submit = SubmitField('Andikisha')

# Sending sms (s) to the users in the system, here.
class SendSMS(FlaskForm):
    """
    Form for sending SMS.
    """
    PhoneNumber = QuerySelectField(query_factory=lambda: Employee.query.all(), get_label="email")
    message     = TextAreaField("Enter the message", validators=[DataRequired()])
    submit      = SubmitField("Send")

# Publishing the products of the of the coop here.
class ProductForm(FlaskForm):
    name = StringField("Product name", validators=[DataRequired()])
    description = TextAreaField("Descriptions", validators=[DataRequired()])
    price       = StringField("The price", validators=[DataRequired()])
    image       = FileField("Image")
    submit      = SubmitField("Submit")

# This is the table which will hold all the information of the projects we are currently working on.
class ProjectForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    duration    = StringField("Duration", validators=[DataRequired()])
    submit      = SubmitField("Submit")

# This is the table which will hold all the information related to our clients
class ClientForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    business = StringField("Business", validators=[DataRequired()])
    submit   = StringField("Submit")

# Form to add new employee in the cooperative is here.
class NewEmployee(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    FirstName = StringField("First name", validators=[DataRequired()])
    LastName  = StringField("Last Name", validators=[DataRequired()])
    #dept  = StringField("Cooperative", validators=[DataRequired()])
    #dept = QuerySelectField(query_factory=lambda: Department.query.filter_by(email=current_user.email),
    #get_label="email")
    submit    = SubmitField("Add")

class SubscriptionPlan(FlaskForm):
    subscribe_for = StringField("Subscribe For", validators=[DataRequired()])
    description   = TextAreaField("Descriptions", validators=[DataRequired()])
    subscribe_plan = StringField("Subscription Plan", validators=[DataRequired()])
    subscription_date = DateTimeField("Subscription Date", validators=[DataRequired()])
    credit_card_no    = StringField("Credit Card no", validators=[DataRequired()])
    submit            = SubmitField("Subscribe")

class ProductForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    description = TextAreaField("Product Descriptions", validators=[DataRequired()])
    quantity    = StringField("Product Quantity", validators=[DataRequired()])
    in_date     = StringField("Entry Date", validators=[DataRequired()])
    status      = StringField("Prouct Status", validators=[DataRequired()])
    submit      = SubmitField("Submit")

class OrderForm(FlaskForm):
    name = StringField("Order Name", validators=[DataRequired()])
    product = QuerySelectField(query_factory=lambda: Product.query.filter_by(department_id=current_user.email),
                                get_label="name")
    description = TextAreaField("Order Descriptions", validators=[DataRequired()])
    quantity    = StringField("Order Quantity", validators=[DataRequired()])
    in_date     = StringField("Date", validators=[DataRequired()])
    status      = StringField("Order Status", validators=[DataRequired()])
    submit      = SubmitField("Submit")

class RepForm(FlaskForm):
    status = SelectField(
        'status',
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In progress'), ('Decided', 'Decided')])
    #status    = StringField("Status", validators=[DataRequired()])
    report_name =  StringField("ReportName", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    owner = QuerySelectField(query_factory=lambda: Employee.query.filter_by(first_name=current_user.first_name), get_label="first_name")
    stakeholders = StringField("Stakeholders", validators=[DataRequired()])
    created_date    =  StringField("Created date", validators=[DataRequired()])
    description  =  StringField("Description", validators=[DataRequired()])
    submit      =  SubmitField('Create')
    def __repr__(self):
        return '<RepForm: {}>'.format(self.owner)

class HowtoForm(FlaskForm):
    name =  StringField("Title", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    labels = QuerySelectField(query_factory=lambda: Employee.query.filter_by(first_name=current_user.first_name), get_label="first_name")
    description = TextAreaField("Descriptions", validators=[DataRequired()])
    steps    =  StringField("Step-by-step Guide", validators=[DataRequired()])
    file  =  FileField("File")
    submit      =  SubmitField('Publish')

class LinkForm(FlaskForm):
    link =  StringField("Link", validators=[DataRequired()], render_kw={"placeholder": "Paste a link to any website"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    title =  StringField("Title", validators=[DataRequired()], render_kw={"placeholder": "Title of the page"})
    labels =  StringField("Labels", validators=[DataRequired()], render_kw={"placeholder": "Suggest a page"})
    sharewith =  StringField("Share With", validators=[DataRequired()], render_kw={"placeholder": "Share this page with users"})
    comment = TextAreaField("Descriptions", validators=[DataRequired()], render_kw={"placeholder": "Share your thoughts about this link"})
    submit      =  SubmitField('Share')

class FileForm(FlaskForm):
    name =  StringField("Name", validators=[DataRequired()], render_kw={"placeholder": "Enter the name of the file"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    description = TextAreaField("Descriptions", validators=[DataRequired()], render_kw={"placeholder": "Enter the description of the shared file"})
    recipe_image = FileField('Recipe Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    submit      =  SubmitField('Upload')

class contributionForm(FlaskForm):
    #status = SelectField(
        #'status',
        #choices=[('nt', 'Not Started'), ('ip', 'In progress'), ('dc', 'Decided')])
    contributor =  StringField("Contributor", validators=[DataRequired()])
    contributionFor = SelectField(
        'Contribution for',
        choices=[('Saving', 'Saving'), ('Daily Contribution', 'Daily Contribution'),
         ('Weekly Contribution', 'Weekly Contribution'), ('Activities', 'Activities'),
         ('Others', 'Others')])
    amount =  StringField("Amount", validators=[DataRequired()])
    #owner    =  StringField("Owner", validators=[DataRequired()])
    comment = TextAreaField("Comment", validators=[DataRequired()])
    #department_id  =  StringField("Department Id", validators=[DataRequired()])
    submit      =  SubmitField('Save')

class bankAccountForm(FlaskForm):
    memberId =  StringField("Member ID", validators=[DataRequired()], render_kw={"placeholder": "Enter Member ID"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    memberName =  StringField("Member Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Name"})
    bankAccountNumber =  StringField("Bank Account", validators=[DataRequired()], render_kw={"placeholder": "Enter Bank Account Name"})
    accountType =  StringField("Account Type", validators=[DataRequired()], render_kw={"placeholder": "Enter Account Type"})
    amount = StringField("Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter amount"})
    date = StringField("Date", validators=[DataRequired()], render_kw={"placeholder": "Enter Date"})
    submit   = SubmitField("Add Account")

class LoanForm(FlaskForm):
    memberId =  StringField("Enter Member Id", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Id"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    memberName =  StringField("Enter Member Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Name"})
    introducer1Id =  StringField("Enter Introducer one ID", validators=[DataRequired()], render_kw={"placeholder": "Enter Introducer one ID"})
    introducer1Name =  StringField("Enter Introducer One Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Introducer One Name"})
    introducer1BankAccountBalance = StringField("Enter Introducer one bank account number", validators=[DataRequired()], render_kw={"placeholder": "Enter Introducer one bank account balance"})
    introducer1Share =  StringField("Enter Introducer oene shares", validators=[DataRequired()], render_kw={"placeholder": "Enter Introducer one shares"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    introducer2Id =  StringField("Introducer Two ID", validators=[DataRequired()], render_kw={"placeholder": "Enter Introducer two ID"})
    introducer2Name =  StringField("Introducer two name", validators=[DataRequired()], render_kw={"placeholder": "Enter Introducer two Name"})
    introducer2BankAccountBalance = StringField("Introducer Two Bank Account balance", validators=[DataRequired()], render_kw={"placeholder": "Enter Introducer two bank account balance"})
    introducer2Share =  StringField("Introducer Two Share", validators=[DataRequired()], render_kw={"placeholder": "Enter Introducer two shares"})
    loanAmount =  StringField("Loan Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter Loan Amount"})
    interestRate =  StringField("Interest Rate", validators=[DataRequired()], render_kw={"placeholder": "Enter Interest Rate"})
    durationInDay =  StringField("Enter Duration", validators=[DataRequired()], render_kw={"placeholder": "Enter Duration In Day"})
    remarksIfAny = StringField("Enter Remarks", validators=[DataRequired()], render_kw={"placeholder": "Enter Remarks If Any"})
    loanType =  StringField("Loan type", validators=[DataRequired()], render_kw={"placeholder": "Enter Loan Type"})
    totalLoanWithInterest =  StringField("Total Loan with Interest", validators=[DataRequired()], render_kw={"placeholder": "Enter Total Loan with Interest"})
    activedBy =  StringField("Active By", validators=[DataRequired()], render_kw={"placeholder": "Active By"})
    loanIssueDate = StringField("Loan Issue Date", validators=[DataRequired()], render_kw={"placeholder": "Enter loan issue Date"})
    submit      =  SubmitField('Apply Loan')

class fixedD(FlaskForm):
    memberId =  StringField("Enter Member Id", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Id"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    memberName =  StringField("Enter Member Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Name"})
    fixedDepositAmount = StringField("Enter Fixed Deposit Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter Fixed Deposit Amount"})
    durationInDay =  StringField("Enter Duration in Day", validators=[DataRequired()], render_kw={"placeholder": "Enter Duration in Day"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    fixedDepositInterest =  StringField("Enter Deposit Interest", validators=[DataRequired()], render_kw={"placeholder": "Enter Deposit Interest"})
    maturityDate =  StringField("Enter Maturity Date", validators=[DataRequired()], render_kw={"placeholder": "Enter Maturity Date"})
    matureAmount = StringField("Enter Mature Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter Mature Amount"})
    createdBy =  StringField("Created By", validators=[DataRequired()], render_kw={"placeholder": "Created By"})
    date = StringField("Created Date", validators=[DataRequired()], render_kw={"placeholder": "Created Date"})
    submit      =  SubmitField('Add Fixed Deposit Account')

class transactionForm(FlaskForm):
    bankAccountNumber =  StringField("Enter Bank Account Number", validators=[DataRequired()], render_kw={"placeholder": "Enter Bank Account Number"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    memberName =  StringField("Enter Member Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Name"})
    accountType = StringField("Enter Account Type", validators=[DataRequired()], render_kw={"placeholder": "Enter Account Type"})
    depositOrWithdraw = SelectField('Select Deposit / WithDraw', choices=[('sl', 'Select'), ('dp', 'Deposit'), ('wd', 'Withdraw')])
    #depositOrWithdraw =  StringField("Select, Deposit or Withdraw", validators=[DataRequired()], render_kw={"placeholder": "Select, Deposit or Withdraw"})
    #owner    =  StringField("Owner", validators=[DataRequired()])
    cashOrCheque = SelectField('Select Cash / Cheque', choices=[('sl', 'Select'), ('ch', 'Cash'), ('cq', 'Cheque')])
    #cashOrCheque =  StringField("Select, Cash or Cheque", validators=[DataRequired()], render_kw={"placeholder": "Select, Cash or Cheque"})
    amount =  StringField("Enter Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter Amount"})
    balance = StringField("Balance", validators=[DataRequired()], render_kw={"placeholder": "Balance"})
    date = StringField("Created Date", validators=[DataRequired()], render_kw={"placeholder": "Created Date"})
    submit      =  SubmitField('Accept')

class shareForm(FlaskForm):
    memberId =  StringField("Enter Member ID", validators=[DataRequired()], render_kw={"placeholder": "Enter Member ID"})
    shareAccNo =  StringField("Enter Member Share Account", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Share Account"})
    memberName =  StringField("Enter Member Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Name"})
    depositOrWithdraw = SelectField('Select Deposit / WithDraw', choices=[('sl', 'Select'), ('dp', 'Deposit'), ('wd', 'Withdraw')])
    shareAmount = StringField("Enter Share Amount", validators=[DataRequired()], render_kw={"placeholder": "Enter Share Amount"})
    balanceShare = StringField("Balance Share", validators=[DataRequired()], render_kw={"placeholder": "Balance Share"})
    date = StringField("Created Date", validators=[DataRequired()], render_kw={"placeholder": "Created Date"})
    submit      =  SubmitField('Add Share')

class installmentForm(FlaskForm):
    memberId =  StringField("Enter Member ID", validators=[DataRequired()], render_kw={"placeholder": "Enter Member ID"})
    loanId =  StringField("Enter Loan ID", validators=[DataRequired()], render_kw={"placeholder": "Enter Loan ID"})
    memberName =  StringField("Enter Member Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Member Name"})
    lastInstallmentPay = StringField("Last Installment Pay", validators=[DataRequired()], render_kw={"placeholder": "Last Installment Pay"})
    lastInstallmentPayDate = StringField("Last Installment Pay Date", validators=[DataRequired()], render_kw={"placeholder": "Last Installment Pay Date"})
    cashOrCheque = SelectField('Select Cash / Cheque', choices=[('sl', 'Select'), ('ch', 'Cash'), ('cq', 'Cheque')])
    payLoanInstallment  = StringField("Pay Loan Installment", validators=[DataRequired()], render_kw={"placeholder": "Pay Loan Installment"})
    balance = StringField("Balance", validators=[DataRequired()], render_kw={"placeholder": "Balance"})
    remarksIfAny = StringField("Enter Remark If Any", validators=[DataRequired()], render_kw={"placeholder": "Enter Remark If Any"})
    date = StringField("Created Date", validators=[DataRequired()], render_kw={"placeholder": "Created Date"})
    submit      =  SubmitField('Make Payment')

