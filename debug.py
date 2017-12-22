from globalx import *

def get_str(val):
	if (val == F or val == FI):
		return ("False")
	if (val == V or val == VI):
		return ("True")
	if (val == INDEF):
		return ("Undetermined")
