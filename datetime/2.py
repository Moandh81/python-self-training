#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to determine whether a given year is a leap year.

import calendar



year = ""


while year.isdigit() == False:
	year = input('Please input the year : \n')





if calendar.isleap(int(year)):
	print("The year " + str(year) + " is leap")
else :
	print("The year " + str(year) + " is not leap")