from . import aicos_stack

@aicos_stack.route('/')
def home():
	return "Hello Stack, there!"