#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to count the number of characters (character frequency)
#  in a string. Go to the editor 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


frequency = {}



text = 'google.com'


for letter in text:
	if letter in frequency.keys():
		frequency[letter] += 1
	else:
		frequency[letter] = 1


print(frequency)
