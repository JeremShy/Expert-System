from globalx import *
from is_x import *
from logic_error import *
from parse_error import *
from simple_logic import *

def is_true_with_dico(expression, dico):
	return is_true(expression, dico.copy())

def buffer_as_value(buffer):
	p = 0
	ret = 0
	for k, i in buffer.items():
		if (i == VI or i == V):
			ret += 2**p
		p += 1
	return ret

def check_column(number, values):
	p = 2 ** number
	for i in values:
		if (p & i):
			if i - p not in values:
				return (False)
		else:
			if i + p not in values:
				return (False)
	return (True)

def analyze_bruteforce(lst):
	if len(lst) == 0:
		raise LogicError("")
	values = []
	for i in lst:

		values.append(buffer_as_value(i))

	useless = []
	for i in range(len(lst[0])):
		if (check_column(i, values) == True):
			useless.append(True)
		else:
			useless.append(False)
	rezone = 0
	rezzero = 0
	debut = False
	for v in values:
		if (debut == False):
			rezone = v
			rezzero = ~v
			debut = True
		rezone &= v
		rezzero &= ~v
	rez = []
	for i in range(len(lst[0])):
		if (2**i & rezone):
			rez.append(V)
		elif (2**i & rezzero):
			rez.append(F)
		elif (useless[i]):
			rez.append(FI)
		else:
			rez.append(INDEF)

	i = 0
	ret = {}
	for k, v in lst[0].items():
		ret[k] = rez[i]
		i += 1
	return ret


def exec_as_true(expression, dico, undefined):
	bruteforce_dico = dico.copy()
	bruteforce_dico = dict(map(lambda ((k, v)): (k, FI) if (v == VI or v == INDEF) else (k, v), bruteforce_dico.items()))
	tmp = dico.copy()
	tmp = {i:0 for i in tmp}
	for i in expression:
		if (is_fact(i)):
			tmp[i] = 1
	bruteforce_dico = dict(filter(lambda ((k, v)) : tmp[k] == 1, bruteforce_dico.items()))
	rez = []
	while (True):
		tmp = is_true_with_dico(expression, bruteforce_dico)
		if (tmp == VI or tmp == V):	
			rez.append(bruteforce_dico.copy())
		for key, c in bruteforce_dico.items():
			if (c == FI):
				bruteforce_dico[key] = VI
				break
			elif (key == bruteforce_dico.keys()[-1]):
				ret = analyze_bruteforce(rez)
				diff = False
				for key, value in ret.items():
					old_value = dico[key]
					if dico[key] == INDEF and (ret[key] == FI or ret[key] == VI):
						pass
					else:
						if undefined == True and ret[key] == F and dico[key] != F:
							dico[key] = FI
						elif undefined == True and ret[key] == V and dico[key] != V:
							dico[key] = VI
						else:
							dico[key] = ret[key]
					if (dico[key] != old_value):
						diff = True
				return diff
			elif (c == VI):
				bruteforce_dico[key] = FI
