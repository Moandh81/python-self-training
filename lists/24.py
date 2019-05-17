#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to append a list to the second list


liste1 = ["cat", "dog", "mouse"]
liste2 =["lion", "tiger", "elephant", "zebra"]

if isinstance(liste2,list):
	for item in liste2:
		liste1.append(item)

print("The new list is : \n" + str(liste1) )