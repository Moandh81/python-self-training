#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Write a Python program to capitalize first and last letters of each word of a given string.



txt = input('Please insert a text : \n')
txt = txt.strip()

newtxt = txt[0].upper() + txt[1:len(txt)-1] + txt[len(txt)-1].upper()

print(newtxt)


