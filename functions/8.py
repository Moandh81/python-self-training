#!/usr/bin/env python
# -*- coding: utf-8 -*


# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


sample = [1,2,3,3,3,3,4,5]

newlist = []


def listOfUniqueElements(mylist):
	if isinstance(mylist,list):
		newset = set(mylist)
		for element in newset:
			newlist.append(element)
		print(newlist)
	else:
		print("The element you introduced is not a list")




listOfUniqueElements(sample)