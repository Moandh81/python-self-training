#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to convert a tuple to a string


mytuple = ("apple", "banana" , "cherry", 12, [1,2,3], {"name": "anis"})
newtxt =''


for item in mytuple:
	newtxt = newtxt + str(item)


print(newtxt)