#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to replace whitespaces with an underscore and vice versa.

import re

sample = "This is a sample string with no __main__"

expression1 =r'\s'
expression2 = r'_'

output =''


for letter in sample:
	if re.match(expression1, letter):
		output = output + '_'

	elif re.match(expression2, letter):
		output = output + ' '

	else:
		output = output + letter



print(output)
