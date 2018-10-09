from flask import render_template
from . import aicos_acc

@aicos_acc.route('/')
def aicos_acc_home():
	return render_template("indexxx.html")


@aicos_acc.route('/income')
def aicosAccIncome():
	return render_template("acc_incomex.php")


@aicos_acc.route('/expense')
def aicosAccExpense():
	return render_template("acc_expensex.html")


@aicos_acc.route('/rentfees')
def aicosAccRentFees():
	return render_template("rent_feesx.html")


@aicos_acc.route('/allincome')
def allIncome():
	return render_template("income/all_incomex.html")



@aicos_acc.route('/newInvoice')
def newInvoice():
	return render_template("income/new_invoicex.html")

@aicos_acc.route('/printInvoice')
def printInvoice():
	return render_template("income/printx.html")


@aicos_acc.route('/newClient')
def newClient():
	return render_template("income/new_clientx.html")


@aicos_acc.route('/newProduct')
def newProduct():
	return render_template("income/new_productx.html")


@aicos_acc.route('/newSponsor')
def newSponsor():
	return render_template("income/new_sponsorx.html")



@aicos_acc.route('/newCapital')
def newCapital():
	return render_template("income/new_capitalx.html")


@aicos_acc.route('/allexpenses')
def allExpenses():
	return render_template("expenses/all_expensesx.html")

@aicos_acc.route('/newBill')
def newBill():
	return render_template("expenses/new_billx.html")



@aicos_acc.route('/newVendor')
def newVendor():
	return render_template("expenses/new_vendorx.html")



@aicos_acc.route('/newProductExpense')
def newProductEx():
	return render_template("expenses/new_productx.html")


@aicos_acc.route('/newLoan')
def newLoan():
	return render_template("expenses/new_loanx.html")



@aicos_acc.route('/allAssets')
def allAssets():
	return render_template("assets/all_assetsx.html")



@aicos_acc.route('/templates')
def templates():
	return render_template("templates/templatesx.html")
