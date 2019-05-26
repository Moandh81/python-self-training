#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to read an entire text file.


import os 


if os.path.exists("example.txt") and os.path.isfile("example.txt"):
	obFichier = open("example.txt", "r")
	t = obFichier.readlines()
	for element in t:
		print(element)
	obFichier.close()