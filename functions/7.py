#!/usr/bin/env python
# -*- coding: utf-8 -*


# Write a Python function that accepts a string and calculate the number of upper case letters
# and lower case letters.
# Expected Output : 
# No. of Upper case characters : 3
# No. of Lower case Characters : 12



import re

txt = input('Please input a text: \n')


def upperLowerLetters(txt) :
	lowercase = r"[a-zàéèùâêûîôïöë]"
	uppercase = r"[A-Z]"
	lowercaseCounter = uppercaseCounter = 0
	for letter in txt:
		if re.search(lowercase, letter) is not None:
			lowercaseCounter = lowercaseCounter + 1
		if re.search(uppercase, letter) is not None:
			uppercaseCounter = uppercaseCounter + 1 
	print("The number of lowercase letters is {}".format(lowercaseCounter))
	print('The number of uppercase letters is {}'.format(uppercaseCounter))


upperLowerLetters(txt)