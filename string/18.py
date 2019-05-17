#!/usr/bin/env python
# -*- coding: utf-8 -*-



# Write a Python function to get a string made of its first three characters of a specified string. 
# If the length of the string is less than 3 then return the original string. Go to the editor
# Sample function and result : 
# first_three('ipy') -> ipy
# first_three('python') -> pyt



string = input("Please input a string : \n")


def first_three(input):
	if len(input) > 3:
		print(input[0:3])
	else:
		print(input)


first_three(string)