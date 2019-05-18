#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to check if a string contains all letters of the alphabet.



alphabet = "abcdefghijklmnopqrstuvwxyz"

frequency = {}


text = input("Please input a text :  \n")




for letter in alphabet:
	if letter in text.lower():
		frequency[letter] = 1


if len(frequency) == len(alphabet):
	print("This string contains all the letters of the alphabet")
else:
	print("This string does not contain all the letters of the alphabet")