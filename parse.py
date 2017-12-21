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
				if (not (is_fact(line[i + 1]) or line[i + 1] == '(' or line[i + 1] == '!')):
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
	symb = 0
	symbs = ""

	if (len(line) == 0):
		raise ParseException("WTF")
	while (True):
		if (len(line) == 0 or line[0] == ')'):
			return (rez + symbs + last_operand);
		if (symb == 1):
			symbs += "!"
			if (line[0] != '!'):
				symb = 2
		elif (symb == 2):
			rez += symbs
			symb = 0
			symbs = ""
		if (line[0] == '('):
			rez += polonaise_me(line[1:])
			line = go_to_last_par(line[1:])
		elif (is_fact(line[0])):
			rez = rez + line[0];
		elif (line[0] == '!'):
			symb = 1
		elif (len(last_operand) > 0):
			if (line[0] == last_operand[0]):
				rez = rez + line[0]
			elif (line[0] == '+' or (line[0] == '|' and last_operand[0] == '^')):
				last_operand = line[0] + last_operand
			else:
				rez = rez + last_operand
				last_operand = line[0]
		else:
			last_operand = line[0]
		line = line[1:];

def get_polonaise(line):
	if (len(line) == 0):
		print "Parse error : member missing"
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
