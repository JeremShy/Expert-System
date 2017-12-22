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
		elif (val1 == FAUX_I or val2 == FAUX_I)
			stack.append(FAUX_I)
		elif (val1 == FAUX or val2 == FAUX)
			stack.append(FAUX)
		elif (val1 == VRAI_I or val2 == VRAI_I)
			stack.append(VRAI_I)
		else
			stack.append(VRAI)
	elif (operand == '|'):
		if (val1 == VRAI or val2 == VRAI):
			stack.append(VRAI)
		elif (val1 == VRAI_I or val2 == VRAI_I):
			stack.append(VRAI_I)
		elif (val1 == INDEF or val2 == INDEF):
			stack.append(INDEF)
		elif (val1 == FAUX_I or val2 == FAUX_I):
			stack.append(FAUX_I)
		else
			stack.append(FAUX)
	elif (operand == '^'):
		if (val1 == INDEF or val2 == INDEF):
			stack.append(INDEF)
		elif ((val1 == VRAI or val1 == FAUX) and (val2 == VRAI or val2 == FAUX)):
			if (val1 == val2):
				stack.append(FAUX)
			else
				stack.append(VRAI)
		else:
			if (val1 == val2):
				stack.append(FAUX_I)
			else
				stack.append(VRAI_I)


def is_true(expression):
	stack = []
	while (True):
		if (len(expression) == 0):
			return stack.pop()
		if (is_fact(expression[0])):
			stack.append(dico[expression[0]])
		elif (is_b_operand(expression[0])):
			exec_operand(stack, expression[0])
			print stack
		elif (expression[0] == '!'):
			value = stack.pop()
			if (value == VRAI):
				value = FAUX
			elif (value == FAUX):
				value = VRAI
			elif (value == FAUX_I):
				value = VRAI_I
			elif (value == VRAI_I):
				value = FAUX_I
			stack.append(value)
		expression = expression[1:]

def is_true_with_dico(expression, other):
	global dico
	save = dico
	dico = other
	is_true(expression)
	dico = save

def exec_as_true(expression):
	global dico


def find_all_possibilities(expression):
	dico_list = []
