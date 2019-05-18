#!/usr/bin/env python
# -*- coding: utf-8 -*-



# Write a Python program to count the occurrences of each word in a given sentence. 


sentence = input("Please input a sentence : \n")

liste = sentence.split(' ')

frequency = {}

for word in liste:
	if word.lower() not in frequency.keys():
		frequency[word.lower()] = 1
	else:
		frequency[word.lower()] = frequency[word.lower()] + 1


print('Here are the frequencies of each word in the sentence : \n')
print('----------------------------------------------------------')

for key, value in frequency.items():
	print(key + " : " + str(value) )
