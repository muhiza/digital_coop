from . import aicos_monitor

@aicos_monitor.route('/')
def home():
	return "Hello Monitor here!"