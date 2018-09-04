from globalx import *

def get_str(val):
	if (val == F or val == FI):
		return ("False")
	elif (val == V or val == VI):
		return ("True")
	else:
		return ("Undetermined")
