#!/usr/bin/env python
# -*- coding: utf-8 -*

# Write a Python function to find the Max of three numbers.


import re

expression =  r'[0-9]+'

numberslist = []

number1 = number2 = number3 = ""

while re.search(expression, number1) is None:
	number1 = input('Please input first number: \n')



while re.search(expression, number2) is None:
	number2 = input('Please input second number: \n')



while re.search(expression, number3) is None:
	number3 = input('Please input third number: \n')



numberslist.append(number1)
numberslist.append(number2)
numberslist.append(number3)

print(numberslist)

print("the maximum number is {}".format(max(numberslist)))