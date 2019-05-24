#!/usr/bin/env python
# -*- coding: utf-8 -*-


 # Write a Python program to find the index of an item of a tuple 


mytuple = ("dog", "cat", "cow", "fox", "hen", "cock", "lion" , "zebra","duck" ,"bull", "sheep", "cat", "cow", "fox", "lion")




item = input('Please input an item : \n')


if item in mytuple:
	print(mytuple.index(item))