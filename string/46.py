#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to convert a string in a list


txt = input('Please input a text : \n')

liste = []


for letter in txt:
	liste.append(letter)

print(liste)