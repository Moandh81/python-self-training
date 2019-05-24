#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to remove item(s) from set if it is in the set

myset = {"apple", "banana", "cherry"}


item = input('Please input an item : \n')


if item in myset:
	myset.remove(item)

print(myset)