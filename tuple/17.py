#!/usr/bin/env python
# -*- coding: utf-8 -*-


 # Write a Python program to unzip a list of tuples into individual lists.

myliste = [(1,2,3),("dog", "cat", "cow", "fox", "hen", "cock", "duck" ,"bull", "sheep") , ("joey", "brianna", 345)]


newliste = []

for element in myliste:
	if isinstance(element, tuple):
		for item in element:
			newliste.append(item)
	else:
		newliste.append(element)



print(newliste)