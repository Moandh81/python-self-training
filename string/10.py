#!/usr/bin/env python
# -*- coding: utf-8 -*-


 # Write a Python program to change a given string to a new string
  # where the first and last chars have been exchanged.

txt = "This is a sample string"

txt2list = list(txt)

newtxt = ""

newtxt = newtxt + txt[len(txt) -1]

i = 1

while i < len(txt) -1:
	newtxt = newtxt + txt[i]
	i = i + 1


newtxt = newtxt + txt[0]


print(newtxt)