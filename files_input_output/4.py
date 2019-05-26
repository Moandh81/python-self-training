#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 4. Write a Python program to read last n lines of a file.


import os 

n = 5

if os.path.exists("example.txt") and os.path.isfile("example.txt"):
	obFichier = open("example.txt", "r")
	t = obFichier.readlines()
	print(t[len(t) -5:])
