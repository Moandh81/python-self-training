#!/usr/bin/env python
# -*- coding: utf-8 -*



#  Write a Python program to count the frequency of words in a file


import os 



frequency = {}

if os.path.exists("example.txt") and os.path.isfile("example.txt"):
	obFichier = open("example.txt", "r")
	t = obFichier.readlines()
	for  line in t:
		words = line.split(' ')
		for word in words:
			if word not in frequency:
				frequency[word] = 1
			else:
				frequency[word] = frequency[word] + 1


frequency.pop("\n", None)

print(frequency)
