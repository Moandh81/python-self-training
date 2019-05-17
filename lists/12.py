#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 

# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


liste = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


if len(liste) >=6:
	del liste[5]
	del liste[4]
	del liste[0]
	print(liste)
elif len(liste) == 5:
	del liste[4]
	del liste[0]
	print(liste)
elif len(liste) < 5 and len(liste) > 0:
	del liste[0]
	print(liste)

	
	
