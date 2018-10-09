from flask import Flask
from flask import render_template, abort, flash, redirect, url_for, request
from . import aicos_union
from flask_login import current_user, login_required
from ..models import * 
from .forms import *
import flask_excel
import flask_excel as excel
from flask import abort,  request, flash, redirect, render_template, url_for, jsonify
from flask_login import current_user, login_required

def check_admin():
	if not current_user.is_admin:
		abort(403)

def check_union():
	if not current_user.is_union:
		abort(403)


@aicos_union.route('/')
@login_required
def indexUnion():
	check_union()
	departments = Department.query.filter_by(union_id=current_user.email).all()
	employees = Member.query.all()
	all_deps = Department.query.count()
	all_mbs = Employee.query.count()
	all_coperatives = Department.query.filter_by(union_id=current_user.email)
	all_dpts_in_union = Department.query.filter_by(union_id=current_user.email).count()

	return render_template("dashboard_union.html", departments=departments, employees=employees, all_deps=all_deps, all_mbs=all_mbs, all_coperatives=all_coperatives, all_dpts_in_union=all_dpts_in_union) 

@aicos_union.route('/members')
@login_required
def union_cooperatives_members():
	check_admin()
	check_union()
	departments = Department.query.filter_by(union_id=current_user.email).all()
	members = Member.query.filter_by(department_union=current_user.email).all()
	member_male = Member.query.filter_by(department_union=current_user.email, Igitsina='Gabo')
	member_female = Member.query.filter_by(department_union=current_user.email, Igitsina='Gore')
	member_all_count = Member.query.filter_by(department_union=current_user.email).count()
	member_male_count = Member.query.filter_by(department_union=current_user.email, Igitsina='Gabo').count()
	member_female_count = Member.query.filter_by(department_union=current_user.email, Igitsina="Gore").count()
	member_youth = Member.query.filter_by(department_union=current_user.email).filter(Member.tariki_yavukiye >= datetime.date(1986,1,1)).all()
	member_youth_count = Member.query.filter_by(department_union=current_user.email).filter(Member.tariki_yavukiye >= datetime.date(1986,1,1)).count()
	employee = Employee.query.all()


	return render_template("coop_union_members.html", 
		departments=departments, 
		members=members, 
		employee=employee, 
		member_male_count=member_male_count, 
		member_female_count=member_female_count,
		member_all_count=member_all_count,
		member_male=member_male,
		member_female=member_female,
		member_youth=member_youth,
		member_youth_count=member_youth_count)


@aicos_union.route('/cooperatives')
@login_required
def all_cooperatives():
	check_union()
	departments = Department.query.filter_by(union_id=current_user.email).all()
	employees = Member.query.all()
	all_deps = Department.query.count()
	all_mbs = Employee.query.count()
	all_coperatives = Department.query.filter_by(union_id=current_user.email)
	all_dpts_in_union = Department.query.filter_by(union_id=current_user.email).count()
	return render_template("union_cooperatives.html", departments=departments, employees=employees, all_deps=all_deps, all_mbs=all_mbs, all_coperatives=all_coperatives, all_dpts_in_union=all_dpts_in_union)

