#!/usr/bin/env python
# -*- coding: utf-8 -*


# Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 


liste = [1,2,3,4,5]





def sumliste(liste):
	sum = 0
	for item in liste:
		sum = sum + item	
	print("The sum of the numbers in the list is {}".format(sum))  



sumliste(liste)