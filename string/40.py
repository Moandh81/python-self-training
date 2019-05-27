#!/usr/bin/env python
# -*- coding: utf-8 -*-


 # Write a Python program to reverse words in a string.

txt =  "This is a sample string"

words =  txt.split(' ')

i = len(words)

newtxt = ""

while i > 0:
	newtxt = newtxt + words[i-1] + " "
	i = i -1



print(newtxt)

