#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string



import re 

sample = "This a string with numbers 123 456 1 23 8900"


expression = r"[0-9]{1,3}"


sample = sample.split(' ')



for word in sample:
	if re.match(expression, word):
		print(word)
