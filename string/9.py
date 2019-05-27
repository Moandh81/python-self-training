#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to remove the nth index character from a nonempty string


txt = "This is a random string"
n = 5

str2list = list(txt)


del str2list[n-1]


newtxt = ""

for letter in str2list:
	newtxt = newtxt + letter

print(newtxt)