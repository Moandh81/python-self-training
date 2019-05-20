#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to get the maximum and minimum value in a dictionary


dictionnary = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
max = 0
min = dictionnary[1]

for value in dictionnary.values():
	if value > max:
		max = value


print(max)


for value in dictionnary.values():
	if value < min:
		min = value


print(min)