#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to count repeated characters in a string. 
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

sample = 'thequickbrownfoxjumpsoverthelazydog'

frequency = {}


for letter in sample:
	if letter not in frequency:
		frequency[letter] = 1
	else:
		frequency[letter] = frequency[letter] +1



frequency = dict( (k, v) for k,v in frequency.items() if v != 1 )






print(frequency)