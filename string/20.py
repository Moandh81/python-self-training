#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python function to reverses a string if it's length is a multiple of 4.

string = input('Please input a string : \n')

newstring= ''


if len(string) % 4 == 0:
	i = len(string) - 1
	while i >=0:
		newstring = newstring + string[i]
		i = i -1
	print(newstring)

else:
	print("The length of the input is not divisible by 4")
