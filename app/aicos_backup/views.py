from . import aicos_backup

@aicos_backup.route('/')
def home():
	return "Hello World!"
