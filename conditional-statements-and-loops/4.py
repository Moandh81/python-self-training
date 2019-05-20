#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


for i in range(6):
	print("*" * i)
	if i == 5:
		while(i > 0):
			print("*" * (i-1))
			i = i -1
	