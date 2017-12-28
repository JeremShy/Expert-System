# from globalx import *
# from is_x import *
# from logic_error import *
# from parse_error import *
#
# def exec_operand(stack, operand):
# 	val1 = stack.pop()
# 	val2 = stack.pop()
# 	if (operand == '+'):
# 		if (val1 == INDEF or val2 == INDEF):
# 			stack.append(INDEF)
# 		elif (val1 == FI or val2 == FI):
# 			stack.append(FI)
# 		elif (val1 == F or val2 == F):
# 			stack.append(F)
# 		elif (val1 == VI or val2 == VI):
# 			stack.append(VI)
# 		else:
# 			stack.append(V)
# 	elif (operand == '|'):
# 		if (val1 == V or val2 == V):
# 			stack.append(V)
# 		elif (val1 == VI or val2 == VI):
# 			stack.append(VI)
# 		elif (val1 == INDEF or val2 == INDEF):
# 			stack.append(INDEF)
# 		elif (val1 == FI or val2 == FI):
# 			stack.append(FI)
# 		else:
# 			stack.append(F)
# 	elif (operand == '^'):
# 		if (val1 == INDEF or val2 == INDEF):
# 			stack.append(INDEF)
# 		elif ((val1 == V or val1 == F) and (val2 == V or val2 == F)):
# 			if (val1 == val2):
# 				stack.append(F)
# 			else:
# 				stack.append(V)
# 		else:
# 			if (val1 == val2):
# 				stack.append(FI)
# 			else:
# 				stack.append(VI)
#
#
# def is_true(expression):
# 	stack = []
# 	while (True):
# 		if (len(expression) == 0):
# 			return stack.pop()
# 		if (is_fact(expression[0])):
# 			stack.append(dico[expression[0]])
# 		elif (is_b_operand(expression[0])):
# 			exec_operand(stack, expression[0])
# 			# print stack
# 		elif (expression[0] == '!'):
# 			value = stack.pop()
# 			if (value == V):
# 				value = F
# 			elif (value == F):
# 				value = V
# 			elif (value == FI):
# 				value = VI
# 			elif (value == VI):
# 				value = FI
# 			stack.append(value)
# 		expression = expression[1:]
#
# def is_true_with_dico(expression, other):
# 	global dico
# 	save = dico
# 	dico = other
# 	val = is_true(expression)
# 	dico = save
# 	return val
#
# def exec_as_true(expression):
# 	global dico
#
# def solver(expression):
# 	dico_list = []
# 	dico_init = dico.copy()
# 	for c in dico_init:
# 		if (c == V or c == VI):
# 			c = V
# 		if
# 	while (True):
# 		tmp = is_true_with_dico(expression, dico_init);
# 		if (tmp == VI or tmp == V):
# 			dico_list.append(dico_init.copy())
# 		for key, c in dico_init.items():
# 			if (dico_init[key] == FI):
# 				dico_init[key] = VI
# 				break
# 			elif (key == dico_init.keys()[-1] and dico_init[key] == VI):
# 					return (dico_list)
# 			else:
# 				dico_init[key] = FI
