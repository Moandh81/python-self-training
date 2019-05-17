#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python program to select the odd items of a list

liste = ["dog", "cat", "mouse", "cow", "horse", "goat", "ship", "snail"]

i = 0

while i < len(liste):
	if i % 2 != 0:
		print(liste[i])
	i = i +1

