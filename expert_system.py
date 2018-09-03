#!/usr/bin/env python
import sys
import string
import re

from parse_error import ParseException
from logic_error import LogicError
from is_x import *
from rule import *
from parse import *
from logic import *
from globalx import *
from debug import *

def change_dico(other):
	global dico
	dico = other

global dico

if (len(sys.argv) != 2):
	print "usage: " + sys.argv[0] + " <inputfile>"
	sys.exit(1)
try:
	f = open(sys.argv[1], "r")
except IOError as e:
	print "{0}: Cannot open file {1}: {2}".format(sys.argv[0], sys.argv[1], e.strerror)
	sys.exit(1)
data = f.readlines()

rules = []
toSearch = ""

initial_facts = False
facts = ""

for line in data:
	line = line.translate(None, string.whitespace)
	line = re.sub(r"#.*", "", line)

	# print '[' + line + ']'
	if (len(line) == 0):
		continue
	i = line.find("<=>")
	if (i != -1):
		obj = Rule(Rule.IMPL, get_polonaise(line[:i]), get_polonaise(line[i+3:]))
		rules.append(obj)

		obj = Rule(Rule.IMPL, get_polonaise(line[i+3:]), get_polonaise(line[:i]))
		rules.append(obj)

		obj = Rule(Rule.IMPL, get_polonaise(line[i+3:]) + "!", get_polonaise(line[:i]) + "!")
		rules.append(obj)

		obj = Rule(Rule.IMPL, get_polonaise(line[:i]) + "!", get_polonaise(line[i+3:]) + "!")
		rules.append(obj)


	elif (line.find("=>") != -1):
		i = line.find("=>")
		obj = Rule(Rule.IMPL, get_polonaise(line[:i]), get_polonaise(line[i+2:]))
		rules.append(obj)
		obj = Rule(Rule.IMPL, get_polonaise(line[i+2:]) + "!", get_polonaise(line[:i]) + "!")
		rules.append(obj)

	elif (line[0] == "="):
		initial_facts = True
		facts = line[1:]
		for c in line[1:]:
			if (not is_fact(c)):
				print "Error while defining initial facts"
				sys.exit(1)
			dico[c] = 1
	elif (line[0] == "?"):
		for c in line[1:]:
			if (not is_fact(c)):
				print "Error while parsing queries"
				sys.exit(1)
			toSearch += c
	else:
		print "Error : Unrecognized line no <=> or =>."
		sys.exit(1)
if (toSearch == ""):
		print "Error: no queries defined"
		sys.exit(1);

if (initial_facts == False):
		print "Error: No initial facts or = followed by a newline"
		sys.exit(1);

while (True):
	dicopy = dico.copy();

	print "Queries : " + toSearch
	print "Initial facts : " + facts

	changes = True;

	change_dico(dico)
	while (changes == True):
		changes = False
		bidule = False
		for r in rules:
			tmp = is_true_with_dico(r.left, dico)
			if (tmp == V or tmp == VI):
				try:
					if (changes == False):
						changes = exec_as_true(r.right, dico)
					else:
						exec_as_true(r.right, dico)
				except LogicError as e:
					print ("Logic error !")
					sys.exit(1)
				except ParseException as e:
					print ("ParseError : " + e.strerror)
					sys.exit(1)

	if (bidule == False):
		for i in toSearch:
			print (i + " : " + get_str(dico[i]))

	try:
		restart = raw_input("Restart ? (Y/n) : ")
	except:
		print "\nGood bye..."
		sys.exit(0)

	if (restart != "n" and restart != "N"):
		dico = { x:-2 for x in dico}
		try:
			restart = raw_input("New initial facts ? =")
		except:
			print "\nGood bye..."
			sys.exit(0)
		facts = restart
		for c in restart:
			if (not is_fact(c)):
				print "Error while defining initial facts"
				sys.exit(1);
			dico[c] = 1;
		try:
			restart = raw_input("New queries ? (default : don't change) ?")
		except:
			print "\nGood bye..."
			sys.exit(0)
		if (restart != ""):
			toSearch = restart;
		else:
			restart = toSearch
		for c in restart:
			if (not is_fact(c)):
				print "Error while parsing queries"
				sys.exit(1);


	else:
		print "\nGood bye..."
		sys.exit(0)
