#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python function that takes a list of words and returns the length of the longest one


txt = input('Please input a string : \n')
txt = txt.split()
wordlength = {}
max = 0

for word in txt:
	wordlength[word.lower()] = len(word)



for item in wordlength:
 	if 
