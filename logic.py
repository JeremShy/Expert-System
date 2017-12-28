from globalx import *
from is_x import *
from logic_error import *
from parse_error import *

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


def is_true(expression):
	stack = []
	while (True):
		if (len(expression) == 0):
			return stack.pop()
		if (is_fact(expression[0])):
			stack.append(dico[expression[0]])
		elif (is_b_operand(expression[0])):
			exec_operand(stack, expression[0])
			# print stack
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

def is_true_with_dico(expression, other):
	global dico
	save = dico
	dico = other
	val = is_true(expression)
	dico = save
	return val

def rules_true_with_dico(rules, dico):
	for r in rules:
		if (is_true_with_dico(r.left, dico) == V):
			if (is_true_with_dico(r.right, dico) != V):
				return (False)
	return True;

def print_solutions(toSearch, dico_list):
	print (dico_list)
	rez = dict()
	if (len(dico_list) == 0):
		print ("Logic Error !")
		return
	for c in toSearch:
		rez[c] = -5
		for d in dico_list:
			if (d[c] != dico_list[0][c]):
				dico_list[0][c] = -1

	for c in toSearch:
		if (dico_list[0][c] == 1):
			print (str(c) + " : True")
		elif (dico_list[0][c] == 2):
			print (str(c) + " : False")
		else:
			print (str(c) + " : Indef")


def solver(rules, toSearch):
	global dico
	print "calling solver"
	dico_list = []
	for k,v in dico.items():
		if (v == FI):
			dico[k] = F
	dicopy = dico.copy();
	tmp = dico.copy();
	for i in tmp:
		i = 0
	for r in rules:
		for c in r.left:
			if (is_fact(c)):
				tmp[c] = 1
		for c in r.right:
			if (is_fact(c)):
				tmp[c] = 1
	dicopy = dict(filter(lambda ((k,v)): tmp[k] == 1, dicopy.items()))
	while (True):
		if (rules_true_with_dico(rules, dicopy)):
			dico_list.append(dicopy.copy())
		for key, c in dicopy.items():
			if (dicopy[key] == F):
				dicopy[key] = V
				break
			elif (key == dicopy.keys()[-1] and dicopy[key] == V):
					print_solutions(toSearch, dico_list)
					return (dico_list)
			elif (dico[key] != V):
				dicopy[key] = F

def exec_as_true(expression):
	global dico
	changes = False
	while (True):
		if (len(expression) == 0):
			return (changes)
		if (is_fact(expression[0])):
			factval = dico[expression[0]];
			if (factval == 0):
				raise LogicError("Error")
			if (dico[expression[0]] != 1):
				changes = True
				print expression[0] + " devient vrai"
			dico[expression[0]] = 1
		elif (expression[0] != '+' and expression[0] != '(' and expression[0] != ')'):
			raise ParseError("Invalid conclusion")
		expression = expression[1:]
