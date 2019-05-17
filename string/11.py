#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Write a Python program to remove the characters which have odd index values of a given string.


string = input('Please input a string: \n')
newstring = ''

i= 0

while i < len(string):
	if i % 2 != 0:
		newstring = newstring + string[i]
	i = i + 1


print(newstring)

