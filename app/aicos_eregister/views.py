from . import aicos_eregister

@aicos_eregister.route('/')
def home():
	return "Hello Electronic registeration!"