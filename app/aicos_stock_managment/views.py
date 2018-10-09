from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_stock_managment
from flask_login import current_user, login_required
from ..models import * 
from .forms import UmusaruroForm, InyongeramusaruroForm, IbyakoreshejweForm, KonteZaBankForm

import flask_excel
import flask_excel as excel

import nexmo

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

client = nexmo.Client(key='e7096025', secret='ab848459dae27b51')


def check_admin():
    if not current_user.is_admin:
        abort(403)

def check_overall():
    if not current_user.is_overall:
        abort(403)

def check_coop_admin():
    if not current_user.is_coop_admin:
        abort(403)


@aicos_stock_managment.route('/')
@login_required
def dashboard():
    check_admin()
    check_coop_admin()

    return render_template('stock_dashboard.html')


@aicos_stock_managment.route('/stock')
def stock():
    check_admin()
    check_coop_admin()
    employee = Department.query.filter_by(email=current_user.email).first()
    employees = employee.members
    all_member_idd = Umusaruro.member_id
    
    umusaruro_resi = Umusaruro.query.filter_by(department_id=current_user.email).all()
    inyongera = Inyongeramusaruro.query.filter_by(department_id=current_user.email).all()
    ibyakoze = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    member_all = Employee.query.filter_by(department_id=current_user.email).all()

    return render_template('stock_manage.html', member_with_no_umusaruro=member_with_no_umusaruro, umusaruro_resi=umusaruro_resi, member_all=member_all, employees=employees, inyongera=inyongera)


@aicos_stock_managment.route('/umusaruro', methods=['GET', 'POST'])
def umusaruro():
    umusaruro_resi = Umusaruro.query.filter_by(department_id=current_user.email).all()
    return render_template('umusaruro.html', umusaruro_resi=umusaruro_resi)


@aicos_stock_managment.route('/inyongeramusaruro')
def inyongeramusaruro():
    check_admin()
    check_coop_admin()
    inyongera = Inyongeramusaruro.query.filter_by(department_id=current_user.email).all()
    return render_template('inyongeramusaruro.html', inyongera=inyongera)


@aicos_stock_managment.route('/ibyakoreshejwe')
def ibyakoreshejwe():
    check_admin()
    check_coop_admin()
    ibyakoreshejwe = Ibyakoreshejwe.query.filter_by(department_id=current_user.email).all()
    return render_template('ibyakoreshejwe.html', ibyakoreshejwe=ibyakoreshejwe)

@aicos_stock_managment.route('/injiza/umusaruro/<int:id>', methods=['GET', 'POST'])
@login_required
def injizaUmusaruro(id):
    check_admin()
    memberid = Member.query.get_or_404(id)
    member_name = Member.query.filter_by(id=memberid.id).first()
    if memberid is None:
        return redirect(url_for('aicos_stock_managment.stock'))
    form = UmusaruroForm()
    if form.validate_on_submit():
        amazina = member_name.izina_ribanza + " " + member_name.izina_rikurikira
        umusaruro = Umusaruro(
                            amazina= amazina,
                            resi = form.resi.data,
                            zone = form.zone.data,
                            umusaruro=form.umusaruro.data,
                            umuceriWoKurya = form.umuceriWoKurya.data,
                            igiciroCyaKimwe = int(form.igiciroCyaKimwe.data),
                            amafarangaYoGutonoza = form.amafrwYoGutonoza.data,
                            umusanzu = form.umusanzu.data,
                            member_id= member_name.id,
                            department_id = current_user.email
                            )

        try:
            db.session.add(umusaruro)
            db.session.commit()
            flash("Umaze kwandika ikindi gikorwa neza!")
            return redirect(url_for('aicos_stock_managment.umusaruro'))
        except Exception:
            flash("Ntago amakuru watanze yashoboye kwakirwa neza!")
            return redirect(url_for('aicos_stock_managment.injizaUmusaruro', form=form, memberid=memberid, member_name=member_name))
    return render_template('record_umusaruro.html', form=form, memberid=memberid, member_name=member_name)


@aicos_stock_managment.route('/injiza/inyongeramusaruro', methods=['GET', 'POST'])
def injizaInyongeramusaruro():
    check_admin()
    form = InyongeramusaruroForm()
    if form.validate_on_submit():

        inyongeramusaruro = Inyongeramusaruro(
                                    umusaruro_resi=form.resi.data,
                                    BriqueteUnity= form.briquetteKg.data,
                                    BriquetePU= form.briquettePU.data,
                                    DapAndNPKUnity= form.DAPandNPKkg.data,
                                    DapAndNPKpu= form.DAPandNPKpu.data,
                                    KCLUnity= form.KCLkg.data,
                                    KCLpu= form.KCLpu.data,
                                    ImbutoIngano= form.ImbutoKg.data,
                                    ImbutoPU= form.ImbutoPU.data,
                                    RedevanceUbuso= form.redevenceUbuso.data,
                                    RedevancePU= form.redevencePU.data,
                                    ImifukaAgaciro= form.ImifukaKg.data,
                                    ImifukaYishyuwe= form.ImifukaPU.data,
                                    department_id=current_user.email
                                    )

        try:
            db.session.add(inyongeramusaruro)
            db.session.commit()
            flash("Umaze kwinjiza neza inyongeramusaruro!")
            return redirect(url_for('aicos_stock_managment.inyongeramusaruro'))
        except Exception:
            flash("Ntabwo Ibyo wakoze byinjiye neza!")
            return redirect(url_for('aicos_stock_managment.injizaInyongeramusaruro'))

    return render_template('/record_inyongeramusaruro.html', form=form)


@aicos_stock_managment.route('/injiza/ibyakoreshejwe', methods=['GET', 'POST'])
def injizaIbyakoreshejwe():
    check_admin()
    check_coop_admin()
    form = IbyakoreshejweForm()
    if form.validate_on_submit():
        ibyakoreshejwe = Ibyakoreshejwe(
                                umusaruro_resi= form.resi.data,
                                deamAndSup= form.beamSup.data,
                                ibihanoCoop= form.ibihanoCoop.data,
                                APKSAMAKIbihano= form.APIISAMAKIbihano.data,
                                ibiraraneNPKandUREA= form.ibiraraneNPKandUREA.data,
                                umusoroWakarere= form.umusoro.data,
                                kwishyuraItsinda= form.kwishyuraItsinda.data,
                                sheeting= form.Sheeting.data,
                                PandS= form.PIS.data,
                                ibyoYagurijwe= form.umuceriYagurijweUmwakaKUshize.data,
                                ibindiYasbwe= form.ibindi.data,
                                department_id= current_user.email
                                )

        try:
            db.session.add(ibyakoreshejwe)
            db.session.commit()

            flash("Winjije neza ibyakoreshejwe uyu mwaka!")
            return redirect(url_for('aicos_stock_managment.ibyakoreshejwe'))
        except Exception:
            flash("Ibyo mumaze gukora Ntabwo byakunze neza Ongera ugerageze!")
            return redirect(url_for('aicos_stock_managment.injizaIbyakoreshejwe'))

    return render_template('/record_ibyakoreshejwe.html', form=form)


@aicos_stock_managment.route('/banki/konte')
def konteZaBanki():
    check_admin
    check_coop_admin()
    konte = CoopMemberBankAccounts.query.filter_by(department_id=current_user.email).all()
    return render_template("/bankiZacu.html", konte=konte)  

@aicos_stock_managment.route('/injiza/konte', methods=['GET', 'POST'])
def injizaKonte():
    check_admin()
    form = KonteZaBankForm()
    if form.validate_on_submit():
        coopMemberBankAccounts = CoopMemberBankAccounts(
                                    umusaruro_resi= form.resi.data,
                                    memberName= form.izinaryaNyiriKonte.data,
                                    bankName= form.izanaRyaBank.data,
                                    bankAccountNumber= form.numeroYaKonte.data,
                                    department_id=current_user.email)

        try:
            db.session.add(coopMemberBankAccounts)
            db.session.commit()
            flash("Winjije neza nimero ya banki")
            return redirect(url_for('aicos_stock_managment.konteZaBanki'))
        except Exception:
            flash("Ibyo wemeje ntabwo bimeze neza Ongera ugerageze!")
            return redirect(url_for('aicos_stock_managment.injizaKonte'))

    return render_template("/record_bankAccount.html", form=form)      


