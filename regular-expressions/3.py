#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python program that matches a string that has an a followed by one or more b's

import re

txt = "I am a string with absolutely no abbreviation at all"

expression = r"(.*)ab+"

tableau = txt.split(' ')


for word in tableau:
	if re.match(expression, word):
		print(word)