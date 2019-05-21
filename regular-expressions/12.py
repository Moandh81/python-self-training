#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program that matches a word containing 'z'


import re

sample  = "Hello everybody, I am a string with no Zebra  in the zoo eazy nah ?"

expression = r'(.*)z(.*)'

sample = sample.split(' ')



for word in sample:
	if re.match(expression, word, re.IGNORECASE):
		print(word)