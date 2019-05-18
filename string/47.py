#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to lowercase first n characters in a string.


import re 

txt = input("Please input a text : \n ")

n = newtxt =  '' 


expression = r"[0-9]+"
print(re.match(expression, n))


while re.search(expression,n) is None:
	n = input("Please input an integer : \n") 



for letter in txt[:int(n)]:
	letter = letter.lower()
	newtxt = newtxt +letter


newtxt = newtxt + txt[int(n):]

print(newtxt)