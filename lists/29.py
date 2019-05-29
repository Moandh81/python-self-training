#!/usr/bin/env python
# -*- coding: utf-8 -*-



# Write a Python program to get unique values from a list. 


sample = [1, 3, 5, 1, 2, 4, 5, 4, 2]


newlist = []


for element in set(sample):
	newlist.append(element)



print(newlist)