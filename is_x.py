def is_b_operand(c):
	if (c == "+" or c == "|" or c == "^"):
		return (True);
	return (False);

def is_fact(c):
	if not (c.isalpha() and c.isupper()):
		return (False)
	return (True);
