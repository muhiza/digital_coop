from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_req
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

@aicos_req.route('/')
def dashboardqw():
    return render_template('homereq.html')


@aicos_req.route('/governanceBooks')
def governanceBooks():
    return render_template('governanceBooks/governanceBook.html')





@aicos_req.route('/accountingBooks')
def accountingBooks():
    return render_template('accountingBooks/accountingBook.html')




@aicos_req.route('/legalBooks')
def legalBooks():
    return render_template('legalBooks/legalBook.html')


@aicos_req.route('/planningBooks')
def planningBooks():
    return render_template('planningBooks/planningBook.html')




@aicos_req.route('/specialReports')
def specialReports():
    return render_template('specialReports/specialReport.html')





# Listing all from governanceBooks block.
@aicos_req.route('/cooperative/intekoRusangeList')
def intekoRusangeList():
    intekoRusangeList = intekoRusange.query.all()
    return render_template("governanceBooks/intekoRusangeList.html", intekoRusangeList=intekoRusangeList, title="List y'ibyemezo by'inteko rusange")

@aicos_req.route('/cooperative/inamaUbuyoboziList')
def inamaUbuyoboziList():
    inamaUbuyoboziList = inamaUbuyobozi.query.all()
    return render_template("governanceBooks/inamaUbuyoboziList.html", inamaUbuyoboziList=inamaUbuyoboziList, title="List y'ibyemezo by'inama y'ubuyobozi")

@aicos_req.route('/cooperative/inamaUbugenzuziList')
def ubugenzuziList():
    ubugenzuzi = Ubugenzuzi.query.all()
    return render_template("governanceBooks/ubugenzuziList.html", ubugenzuzi=ubugenzuzi, 
                            title="List y'ibyemezo by'inama y'ubugenzuzi")

# Processing forms on the Governance Block.
# This is the views for adding new inteko rusange meeting notes
@aicos_req.route('/cooperative/ibyemezo_byinama', methods=['GET', 'POST'])
@login_required
def intekoRusangeAdd():
    #check_admin()
    form = intekoRusangeForm()
    if form.validate_on_submit():
        inteko = intekoRusange(
                        status1=form.ibyizweho.data,
                        decision1=form.decision1.data,
                        owner1   = form.owner1.data,
                        stakeholders1=form.stakeholders1.data,
                        due_date1=form.due_date1.data,
                        background1 = form.background1.data,
                        department_id = current_user.email
                        )

        try:
            db.session.add(inteko)
            #db.session.add(notif)
            db.session.commit()
            flash("Umaze kubika neza ibyemezo by'inama")
        except:
            flash("Habayeho ikibazo mu makuru watanze!")
        return redirect(url_for('aicos_req.intekoRusangeList'))
    return render_template("governanceBooks/intekoRusange.html", form=form, title="Create")


# This is the views for adding new inama y'ubuyobozi meeting notes
@aicos_req.route('/cooperative/ibyemezoByinamaUbuyobozi', methods=['GET', 'POST'])
@login_required
def inamaUbuyoboziAdd():
    check_admin()
    form = inamaUbuyoboziForm()
    if form.validate_on_submit():
        inama = inamaUbuyobozi(status=form.status.data,
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
            db.session.add(inama)
            db.session.add(notif)
            db.session.commit()
            flash("Umaze kubika neza ibyemezo by'inama")
        except:
            flash("Habayeho ikibazo mu makuru watanze!")
        return redirect(url_for('aicos_req.inamaUbuyoboziList'))
    return render_template("governanceBooks/inamaUbuyobozi.html", form=form, title="Create")





# This is the views for adding new inama y'ubugenzuzi meeting notes
@aicos_req.route('/cooperative/ibyemezoByinamaUbugenzuzi', methods=['GET', 'POST'])
@login_required
def ubugenzuziAdd(*args, **kwargs):
    check_admin()
    form = ubugenzuziForm()
    if form.validate_on_submit():
        inamaUbugenzuzi = Ubugenzuzi(status=form.status.data,
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
            db.session.add(inamaUbugenzuzi)
            db.session.add(notif)
            db.session.commit()
            flash("Umaze kubika neza ibyemezo by'inama")
        except:
            flash("Habayeho ikibazo mu makuru watanze!")
        return redirect(url_for('aicos_req.ubugenzuziList'))
    return render_template("governanceBooks/ubugenzuzi.html", form=form, title="Create")











# Views which are going to be dealing with Accounting Book.
@aicos_req.route('/abanyamuryangoImigabane', methods=['GET', 'POST'])
def abanyamuryangoImigabane():
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
    #if employees is not None:
    #employees = Employee.query.filter_by(email=form.email.data)
    return render_template('accountingBooks/imigabane/abanyamuryangoImigabane.html',
                           employees=employees,
                           employee=employee,
                           employees_count=employees_count,
                           notes = notes,
                           title='Employees')


@aicos_req.route('/abanyamuryangoImigabaneDetails/<int:id>', methods=['GET', 'POST'])
@login_required
def abanyamuryangoDetails(id):
    check_admin()
    employee = Member.query.get_or_404(id)
    if employee is not None:
        return render_template("accountingBooks/imigabane/abanyamuryangoImigabaneDetails.html", employee=employee)
    return redirect(url_for('aicos_req.abanyamuryangoImigabane'))






# Kongera umugabane ku munyamuryango.
@aicos_req.route('/cooperative/umugabane/add/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_umugabane(id):
    """
    Edit a role
    """
    check_admin()
    #add_role = False
    member = Member.query.get_or_404(id)
    form = MemberForm(obj=member)
    if form.validate_on_submit():
        member.firstName = form.firstName.data
        member.nId = form.nId.data
        db.session.add(member)
        db.session.commit()
        flash('Umaze kongera umugabane.')
        # redirect to the roles pagess
        return redirect(url_for('aicos_req.abanyamuryangoImigabane'))
    form.firstName.data = member.firstName
    form.nId.data = member.nId
    return render_template('accountingBooks/imigabane/addUmugabane.html', form=form, title="Edit Umugabane")








# Isanguku views are here.
@aicos_req.route('/cooperative/isanduku')
def isandukuList():
    isanduku = Isanduku.query.all()
    return render_template("accountingBooks/isanduku/isandukuList.html", isanduku=isanduku, title="List y'ibyemezo by'inteko rusange")



@aicos_req.route('/cooperative/add/Isanduku', methods=['GET', 'POST'])
@login_required
def isandukuAdd():
    check_admin()
    form = isandukuForm()
    if form.validate_on_submit():
        isanduku = Isanduku(

                        no=form.no.data,
                        done_date=form.done_date.data,
                        action=form.action.data,
                        income   = form.income.data,
                        expense   = form.expense.data,
                        remain   = form.remain.data,
                        done_by   = form.done_by.data,
                        done_to   = form.done_to.data,
                        department_id = current_user.email
                        )

        notif = Notification(action="Communication",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            """
            to_number = '+250786012383'
            message = current_user.email + ' Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            """

            db.session.add(isanduku)
            db.session.add(notif)
            db.session.commit()
            flash("Wongereye amakuru mu isanduku neza")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_req.isandukuList'))
    return render_template("accountingBooks/isanduku/isanduku.html", form=form, title="Kongera mu Isanduku.")





# Umusaruro views are here.
@aicos_req.route('/cooperative/Umusaruro')
def umusaruroList():
    umusaruro = Umusaruro.query.all()
    return render_template("accountingBooks/umusaruro/umusaruroList.html", umusaruro=umusaruro, title="List y'umusaruro winjiye")



@aicos_req.route('/cooperative/add/Umusaruro', methods=['GET', 'POST'])
@login_required
def umusaruroAdd():
    check_admin()
    form = umusaruroForm()
    if form.validate_on_submit():
        umusaruro = Umusaruro(
                        Amazina=form.Amazina.data,
                        Taliki=form.Taliki.data,
                        Uwagemuye=form.Uwagemuye.data,
                        Ibiro   = form.Ibiro.data,
                        Igiciro   = form.Igiciro.data,
                        IkiguziCyose   = form.IkiguziCyose.data,
                        amafarangaYishyuweKuKiro   = form.amafarangaYishyuweKuKiro.data,
                        done_by   = form.done_by.data,
                        done_to   = form.done_to.data,
                        department_id = current_user.email
                        )



        notif = Notification(action="Communication",
                            done_by=current_user.username,
                            done_from=IP,
                            done_time = "frank",
                            done_to="tapayi",
                            effect = "system upgraded",
                            department_id = current_user.email)
        try:
            """
            to_number = '+250786012383'
            message = current_user.email + ' Decision has made and you are concerned'
            response = client.send_message({'from' : '+250786012383', 'to' : to_number, 'text' : message })
            response_text = response['messages'][0]
            """

            db.session.add(umusaruro)
            db.session.add(notif)
            db.session.commit()
            flash("Winjije neza umusaruro muri Cooperative")
        except:
            flash("Error! Invalid information")
        return redirect(url_for('aicos_req.umusaruroList'))
    return render_template("accountingBooks/umusaruro/umusaruro.html", form=form, title="Kongera umusaruro muri Cooperative.")








# Views for the Wide Cooperative Market.
@aicos_req.route('/cooperatives/wcm')
def wcmIndex():
    umusaruro = Umusaruro.query.all()
    return render_template('accountingBooks/wcm/index.html', umusaruro=umusaruro)




@aicos_req.route('/AccountingBook')
def abishyuye():

    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    employees_count = employee.members.count()


    return render_template('accountingBooks/abishyuye/abishyuyeList.html',
                            employees=employees, title='List yabanyamuryango bishyuye!')









# Views for the Wide Cooperative Market.
@aicos_req.route('/cooperatives/ibitaboBank')
def bankIbitabo():
    bankIbitaboList = ibitaboBank.query.all()
    return render_template('accountingBooks/ibitaboBank/ibitaboBankList.html', bankIbitaboList=bankIbitaboList)






# ibitabo bya banks.
@aicos_req.route('/accountingBooks/BankBooks', methods=['GET', 'POST'])
def ibitaboBank():
    form = ibitaboBankForm()
    if form.validate_on_submit():
        ibitabo = ibitaboBank(
                                no = form.No.data,
                                date = form.Date.data,
                                igikorwa = form.Igikorwa.data,
                                debt     = form.Debit.data,
                                credit   = form.Credit.data,
                                solde    = form.Solde.data,
                                department_id = current_user.email)
        try:
            db.session.add(ibitabo)
            db.session.commit()
            flash("Umaze kwinjize igitabo cya bank neza!")
            return redirect(url_for('aicos_req.ibitaboBankList'))
        except:
            flash("Ntago igitabo cyabashije kwinjira neza!")
    return render_template('accountingBooks/ibitaboBank/ibitaboBank.html', form=form, title="List y'ibitabo bya banks!")





@aicos_req.route('/cooperatives/accountingBook/BankHistoty')
def bankHistory():
    return render_template('accountingBooks/bankHistory/bankHistory.html')




@aicos_req.route('/cooperatives/accountingBook/signatories')
def signatories():
    return render_template('accountingBooks/bankHistory/signatories.html')