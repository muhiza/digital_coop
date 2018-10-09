from flask import Flask, render_template, flash
from . import aicos_wcm


@aicos_wcm.route('/aicos/WideCooperativeMarket')
def indexWcm():
	return render_template("frontEnd/index.html")