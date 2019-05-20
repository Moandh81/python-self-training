#!/usr/bin/env python
# -*- coding: utf-8 -*-



#Write a Python program to find common items from two lists.


list1 = ["john", "jane", "marc", "henry"]
list2 = ["paul", "pedro", "marc", "nadia", "henry"]


for element in list2:
	if element in list1:
		print(element)