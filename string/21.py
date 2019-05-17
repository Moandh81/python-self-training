#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python function
# to convert a given string to all uppercase 
# if it contains at least 2 uppercase characters in the first 4 characters. 


# we have to check first of all for the number of  uppercase characters in a string



import re 

txt = input("Please input a string : \n")

x = re.findall("[A-Z]", txt[0:4])



if len(x) >=2 :
	txt = txt.upper()
	print(txt)

