#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python program that accepts a word from the user and reverse it.


word = input("Please input a word : \n")


newword = ""


i = len(word)

while i > 0:
	newword = newword + word[i-1]
	i = i - 1


print(newword)