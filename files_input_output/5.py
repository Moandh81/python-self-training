#!/usr/bin/env python
# -*- coding: utf-8 -*



# Write a Python program to read a file line by line and store it into a list.



import os 


if os.path.exists("example.txt") and os.path.isfile("example.txt"):
	obFichier = open("example.txt", "r")
	t = obFichier.readlines()
	print(t)