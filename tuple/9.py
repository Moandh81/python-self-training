#!/usr/bin/env python
# -*- coding: utf-8 -*-


 # Write a Python program to find the repeated items of a tuple.


mytuple = ("dog", "cat", "cow", "fox", "hen", "cock", "lion" , "zebra","duck" ,"bull", "sheep", "cat", "cow", "fox", "lion")


frequency = {}





for item in mytuple:
	if item.lower() not in frequency:
		frequency[item.lower()] = 1

	else:
		frequency[item.lower()] = frequency[item.lower()] + 1





for key,value  in frequency.items():
	if frequency[key] > 1:
		print(key)



