from . import aicos_salesio

@aicos_salesio.route('/')
def home():
	return "Hello There on sales io!"