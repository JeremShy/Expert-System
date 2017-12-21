#!/usr/bin/env python
import sys
import string
import re

from parse_error import ParseException
from is_x import *
from rule import *
from parse import *
from logic import *
from globalx import *
from debug import *

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

rules = [];
toSearch = "";

initial_facts = False;

for line in data:
	line = line.translate(None, string.whitespace)
	line = re.sub(r"#.*", "", line)

	# print '[' + line + ']'
	if (len(line) == 0):
		continue
	i = line.find("<=>")
	if (i != -1):
		obj = Rule(Rule.EQU, get_polonaise(line[:i]), get_polonaise(line[i+3:]))
		rules.append(obj);
	elif (line.find("=>") != -1):
		i = line.find("=>")
		obj = Rule(Rule.IMPL, get_polonaise(line[:i]), get_polonaise(line[i+2:]))
		rules.append(obj);
	elif (line[0] == "="):
		initial_facts = True;
		for c in line[1:]:
			if (not is_fact(c)):
				print "Error while defining initial facts"
				sys.exit(1);
			dico[c] = 1;
	elif (line[0] == "?"):
		for c in line[1:]:
			if (not is_fact(c)):
				print "Error while parsing queries"
				sys.exit(1);
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

for obj in rules:
	print obj;

print "Queries : " + toSearch
print "Val : " + get_str(is_true(rules[0].left))


 # A ^ B | C + D => A
 # ABC+D^|
 # ABCD+|^
# A | B | C + D + E | F | G + H + I | J | K
# AB|CD+E+|F|GH+I+|J|K|
# AB|CD+EF|+|GH+IJ|+|K|
