#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to check whether an element exists within a tuple.



mytuple = ("dog", "cat", "cow", "fox", "hen", "cock", "lion" , "zebra","duck" ,"bull", "sheep", "cat", "cow", "fox", "lion")


txt = input("Input a word please : \n")


counter = 0


for element in mytuple:
	if element == txt.lower():
		counter = counter + 1




if counter == 0 :
	print(txt + " does not exist in  the tuple")
else:
	print(txt + " exists in the tuple")