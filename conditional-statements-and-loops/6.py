#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = list(range(37))

odd = even = 0


for number in numbers:
	if number % 2 == 0:
		even = even + 1
	else:
		odd = odd + 1




print("The number of odd numbers is {0} and the number of even numbers is {1}".format(odd, even))