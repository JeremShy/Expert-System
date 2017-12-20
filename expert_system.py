#!/usr/bin/env python
import sys
import string
import re

from parse_error import ParseException
from is_x import *

def check_parenthesis_error(line):
	

def check_for_error(line):
	if (line.count("(") != line.count(")")):
		raise ParseException("parenthesis error")
	for i, c in enumerate(line):
		if (is_b_operand(c)):
			if (i == 0 or i == len(line) - 1):
				raise ParseException("operand error for " + c);
			if (not (is_fact(line[i - 1]) or line[i - 1] == ')') or not (is_fact(line[i + 1]) or line[i + 1] == '(')):
				raise ParseException("operand error for " + c);



###			 	MAIN		#####

if (len(sys.argv) != 2):
	print "usage: " + sys.argv[0] + " <inputfile>"
	sys.exit(1)
try:
	f = open(sys.argv[1], "r")
except IOError as e:
	print "{0}: Cannot open file {1}: {2}".format(sys.argv[0], sys.argv[1], e.strerror)
	sys.exit(1)
data = f.readlines();

for line in data:
	line = line.translate(None, string.whitespace)
	line = re.sub(r"#.*", "", line)

	print '[' + line + ']'
	if (len(line) == 0 or line[0] == '#'):
		continue
	try:
	 	check_for_error(line)
	except ParseException as e:
		print "Error: " + e.strerror
		continue
	print "OK"
