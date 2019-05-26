#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 2. Write a Python program to read first n lines of a file.



import os 


n = 5
i=0

if os.path.exists("example.txt") and os.path.isfile("example.txt"):
	obFichier = open("example.txt", "r")
	t = obFichier.readlines()
	while i < n:
		print(t[i])
		i = i + 1
	obFichier.close()