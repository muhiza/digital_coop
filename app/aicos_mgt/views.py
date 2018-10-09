from . import aicos_mgt

@aicos_mgt.route('/')
def home():
	return "Hello Management related things!"