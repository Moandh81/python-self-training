#!/usr/bin/env python
# -*- coding: utf-8 -*

#  Write a Python program to write a list to a file

liste = ["hello", "Good Bye", "Farewell"]


obFichier = open("testfile.txt", "a")
for element in liste:
	obFichier.write(element + " \n")

obFichier.close()

