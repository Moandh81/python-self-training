#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to convert a string to a list.


string = input('Please input a string : \n')
liste= []

i = 0

while i < len(string):
	liste.append(string[i])
	i = i + 1

print(liste)