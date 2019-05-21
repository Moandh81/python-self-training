#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python program that matches a string that has an a followed by 3 b's

import re

txt = "I am ab string with abbsolutely no abbbreviation at all abbbb"

expression = r"(.*)ab{3}"

tableau = txt.split(' ')


for word in tableau:
	if re.match(expression, word):
		print(word)