#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python function that takes a list of words and returns the length of the longest one


txt = input('Please input a list of words separated by a space : \n')

liste = txt.split(' ')



length = {}

for word in liste:
	length[word] = len(word)

max=  0

for value in length.values():
	if value > max:
		max = value


print("The length of the longest word is : " + str(max) + " characters")