from . import aicos_finance

@aicos_finance.route('/')
def home():
	return "Hello Financial Stuffs!"