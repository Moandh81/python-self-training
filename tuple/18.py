#!/usr/bin/env python
# -*- coding: utf-8 -*-



# Write a Python program to reverse a tuple.


mytuple = ("dog", "cat", "cow", "fox", "hen", "cock", "duck" ,"bull", "sheep")

myliste = []


i = len(mytuple)

while i > 0:
	myliste.append(mytuple[i-1])
	i = i -1


inversedTuple = tuple(myliste)


print(inversedTuple)