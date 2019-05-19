#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to find those numbers 
# which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

import getpass


liste = list(range(1500,2701))




for number in  liste :
	if number % 5 == 0 and number % 7 == 0:
		print(number)




