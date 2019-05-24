#!/usr/bin/env python
# -*- coding: utf-8 -*-

 # Write a Python program to remove an item from a tuple. 

mytuple = ("dog", "cat", "cow", "fox", "hen", "cock", "duck" ,"bull", "sheep")


myliste = []


txt = input("Please input a text : \n")


for element in mytuple:
	if element != txt:
		myliste.append(element)


myliste=tuple(myliste)

print(myliste)