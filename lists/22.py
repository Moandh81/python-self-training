#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to find the index of an item in a specified list

liste = ["hello", "good morning", "good evening", "good night"]

element = input("Please give a specified item to search in the list : \n")



try:
	index =  liste.index(element.lower())
	print(index)

except :
	print("The element you inputted is not in the list")
	