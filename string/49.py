#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to count and display the vowels of a given text

txt = input('Please insert a text : \n')

vowels = ["a", "e", "u", "i", "o", "y", "é", "è", "ù", "à"]

for letter in txt:
	if letter.lower() in vowels:
		print(letter.lower())