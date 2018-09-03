from globalx import *
from is_x import *
from logic_error import *
from parse_error import *
from simple_logic import *

def is_true_with_dico(expression, dico):
	return is_true(expression, dico.copy())

def print_solutions(toSearch, dico_list):
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

def exec_as_true(expression, dico):
	print "expression : " + expression
	bruteforce_dico = dico.copy()
	map(lambda x: FI if (x == VI) else x, bruteforce_dico)
	tmp = dico.copy()
	tmp = {i:0 for i in tmp}
	for i in expression:
		if (is_fact(i)):
			tmp[i] = 1
	bruteforce_dico = dict(filter(lambda ((k, v)) : tmp[k] == 1, bruteforce_dico.items()))

	rez = []

	# print "\npouet"
	# print bruteforce_dico
	# print ""
	while (True):
		# print bruteforce_dico
		tmp = is_true_with_dico(expression, bruteforce_dico)
		if (tmp == VI or tmp == V):
			# print "Appending" + str(bruteforce_dico)
			rez.append(bruteforce_dico.copy())

		for key, c in bruteforce_dico.items():
			if (c == FI):
				bruteforce_dico[key] = VI
				break
			elif (key == bruteforce_dico.keys()[-1]):
				print rez
				return 
			elif (c == VI):
				bruteforce_dico[key] = FI
