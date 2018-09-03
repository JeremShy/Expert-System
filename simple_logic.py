from globalx import *
from is_x import *

def exec_operand(stack, operand):
	val1 = stack.pop()
	val2 = stack.pop()
	if (operand == '+'):
		if (val1 == INDEF or val2 == INDEF):
			stack.append(INDEF)
		elif (val1 == FI or val2 == FI):
			stack.append(FI)
		elif (val1 == F or val2 == F):
			stack.append(F)
		elif (val1 == VI or val2 == VI):
			stack.append(VI)
		else:
			stack.append(V)
	elif (operand == '|'):
		if (val1 == V or val2 == V):
			stack.append(V)
		elif (val1 == VI or val2 == VI):
			stack.append(VI)
		elif (val1 == INDEF or val2 == INDEF):
			stack.append(INDEF)
		elif (val1 == FI or val2 == FI):
			stack.append(FI)
		else:
			stack.append(F)
	elif (operand == '^'):
		if (val1 == INDEF or val2 == INDEF):
			stack.append(INDEF)
		elif ((val1 == V or val1 == F) and (val2 == V or val2 == F)):
			if (val1 == val2):
				stack.append(F)
			else:
				stack.append(V)
		else:
			if (val1 == val2):
				stack.append(FI)
			else:
				stack.append(VI)

def is_true(expression, dico):
	# print "Testing expression " + expression + " with dico " + str(dico)
	stack = []
	while (True):
		if (len(expression) == 0):
			return stack.pop()
		if (is_fact(expression[0])):
			stack.append(dico[expression[0]])
		elif (is_b_operand(expression[0])):
			exec_operand(stack, expression[0])
		elif (expression[0] == '!'):
			value = stack.pop()
			if (value == V):
				value = F
			elif (value == F):
				value = V
			elif (value == FI):
				value = VI
			elif (value == VI):
				value = FI
			stack.append(value)
		expression = expression[1:]
