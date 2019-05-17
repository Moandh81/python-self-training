#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Write a Python program to print the numbers of a specified list after removing even numbers from it. 

liste = list(range(0,100))


for item in liste:
	if item % 2 == 0:
		liste.remove(item)


print(" The new list after removing even numbers is :" + str(liste))