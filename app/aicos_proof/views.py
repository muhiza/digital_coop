from . import aicos_proof

@aicos_proof.route('/')
def home():
	return "Hello Proof There!"