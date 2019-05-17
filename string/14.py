#!/usr/bin/env python
# -*- coding: utf-8 -*-


#  Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically). Go to the editor
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red




string = "cat, dog, bunny, cock, duck, horse , cow, hen, cock, duck, horse, cock, duck, horse"



string = string.split(',')


string2 = [item.strip() for item in string]


tableau = []

for item in string2:
	tableau.append(item)



tableau = sorted(tableau)

print(tableau)

 