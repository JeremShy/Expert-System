#!/usr/bin/env python
import sys
import string
import re

from parse_error import ParseException
from is_x import *
from rule import *

dico = {
				'A' : 0,
				'B' : 0,
				'C' : 0,
				'D' : 0,
				'E' : 0,
				'F' : 0,
				'G' : 0,
				'H' : 0,
				'I' : 0,
				'J' : 0,
				'K' : 0,
				'L' : 0,
				'M' : 0,
				'N' : 0,
				'O' : 0,
				'P' : 0,
				'Q' : 0,
				'R' : 0,
				'S' : 0,
				'T' : 0,
				'U' : 0,
				'V' : 0,
				'W' : 0,
				'X' : 0,
				'Y' : 0,
				'Z' : 0
			}

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
		elif (c != '(' and c != ')'):
			raise ParseException("unknown symbol : " + c);

def go_to_last_par(line):
	i = 1
	while (True):
		if (line[0] == '('):
			i += 1
		if (line[0] == ')'):
			i -= 1
		if (i == 0):
			return (line)
		line = line[1:]


def polonaise_me(line):
	# print ("calling polonaise_me with line : " + line);

	rez = ""
	last_operand = "";
	if (len(line) == 0):
		raise ParseException("WTF")
	while (True):
		if (len(line) == 0 or line[0] == ')'):
			# print "returning : " + rez + last_operand
			return (rez + last_operand);
		elif (line[0] == '('):
			rez += polonaise_me(line[1:])
			# print "line before : " + line
			line = go_to_last_par(line[1:])
			# print "line after : " + line
		elif (is_fact(line[0])):
			rez = rez + line[0];
		elif (line[0] == '+'):	# Prioritaire
			last_operand = line[0] + last_operand;
		else: 					# Non prioritaire
			rez = rez + last_operand
			last_operand = line[0];
		line = line[1:];

def get_polonaise(line):
	if (len(line) == 0):
		print "Parse error"
		sys.exit(1);
	try:
	 	check_for_error(line)
	except ParseException as e:
		print "Parse error: " + e.strerror
		sys.exit(1);
	# print "OK"
	rez = polonaise_me(line);
	# print "rez : " + rez
	return (rez);




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
	else:
		print "Parse error : no second member on a rule"
		sys.exit(1);

for obj in rules:
	print obj;
