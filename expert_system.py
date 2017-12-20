#!/usr/bin/env python
import sys
import string
import re

from parse_error import ParseException
from is_x import *

def check_parenthesis_error(line):
	i = 0
	for c in line:
		if (c == "("):
			b = False
			i = i + 1
		elif (c == ")"):
			if (b == False):
				raise ParseException("parenthesis error: empty parenthesis")
			i = i - 1
		else:
			b = True
		if (i < 0):
			raise ParseException("parenthesis error")
	if (i != 0):
		raise ParseException("parenthesis error")

def check_for_error(line):
	check_parenthesis_error(line)
	if (line[len(line) - 1] == '!'):
		raise ParseException("operand error for !");
	for i, c in enumerate(line):
		if (is_b_operand(c)):
			if (i == 0 or i == len(line) - 1):
				raise ParseException("operand error for " + c)
			if (not (is_fact(line[i - 1]) or line[i - 1] == ')') or not (is_fact(line[i + 1]) or line[i + 1] == '(' or line[i + 1] == '!')):
				raise ParseException("operand error for " + c)
		elif (is_fact(c)):
			if (i != 0):
				if (not (is_b_operand(line[i - 1]) or line[i - 1] == '(' or line[i - 1] == '!')):
					raise ParseException("fact error 1 for " + c)
			if (i != len(line) - 1):
				if (not (is_b_operand(line[i + 1]) or line[i + 1] == ')')):
					raise ParseException("fact error 2 for " + c)
		elif (c == '!'):
			if (i != 0):
				if (not (is_b_operand(line[i - 1]) or line[i - 1] == '(' or line[i - 1] == '!')):
					raise ParseException("operand error 1 for !")
			if (i != len(line) - 1):
				if (not (is_fact(line[i + 1]) or line[i + 1] == '(')):
					raise ParseException("operand error 2 for !")


def polonaise_me(line):
	pass


###			 	MAIN		#####

if (len(sys.argv) != 2):
	print "usage: " + sys.argv[0] + " <inputfile>"
	sys.exit(1)
try:
	f = open(sys.argv[1], "r")
except IOError as e:
	print "{0}: Cannot open file {1}: {2}".format(sys.argv[0], sys.argv[1], e.strerror)
	sys.exit(1)
data = f.readlines()

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
	rez = polonaise_me(line);

# 1 + (2 + 9) * (2 * (1 + 1)) + 3 * (4 * ( 5 + (5 + 0))
