#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a python program to convert camel case string to snake case string.

import re

txt ="camelCase"

expression = r'[a-z0-9]+[A-Z][a-z0-9]+'


txt= txt.split(' ')


neword =""
capital = r"[A-Z]"
	


for word in txt:
	if re.match(expression, word):
		for letter in word:
			if re.match(capital, letter):
				neword =neword + "_" + letter.lower()
			else:
				neword = neword + letter


 	

print(neword)