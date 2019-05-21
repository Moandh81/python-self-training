#!/usr/bin/env python
# -*- coding: utf-8 -*-

 # Write a Python program to find all words starting with 'a' or 'e' in a given string



import re 


sample = "This is a sample text area with the same echo hero"


sample = sample.split(' ')

expression1 = r'a'
expression2 = r'e'


for word in sample:
	if re.match(expression1, word[0].lower()) or re.match(expression2, word[0].lower()) :
		print(word)