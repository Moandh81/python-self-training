#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program which iterates the integers from 1 to 50. For multiples of three 
# print "Fizz" instead of the number 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output : 
# fizzbuzz
# 1
# 2
# fizz
# 4 
# buzz


liste = list(range(1,51))


for number in liste:
	if (number % 3 == 0) and (number % 5 == 0):
		print('fizzbuzz')
	elif (number % 3 == 0) and (number % 5 != 0):
		print("fizz")
	elif (number % 3 != 0) and (number % 5 == 0):	
		print("buzz")
	else:
		print(number)





