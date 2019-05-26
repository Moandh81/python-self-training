#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to append text to a file and display the text.



import os 

txt = input('Please insert a text : \n')

if os.path.exists("example.txt") and os.path.isfile("example.txt"):
	obFichier = open("example.txt", "a")
	obFichier.write("\n"+txt)
	obFichier.close()
