from globalx import *
from is_x import *
from logic import *

def add_dico(dico, prio):
	for k,c in prio.items():
		dico[k] = c
	return (dico)

def merge_list(dico_list):


def recursive(rules, dico):
	for r in rules:
		if (is_true(r.left)):
			possibilities = find_all_possibilities(r.right)
			dico_list = []
			for pos in possibilities:
				dico_list.append(recursive(rules, add_dico(dico, pos)))
# dico = merge_list(dico_list) # dissension


def solver(rules):
	global dico

	rez = recursive(rules, dico)
