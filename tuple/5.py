#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to add an item in a tuple.


mytuple = ("dog", "cat", "cow", "fox", "hen", "cock", "duck" ,"bull", "sheep")

newElement = input('Please insert a text : \n')



mylist = []


for element in mytuple:
	mylist.append(element)


mylist.append(newElement)


print(tuple(mylist))