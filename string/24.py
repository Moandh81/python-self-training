#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python program to check whether a string starts with specified characters

import re


text = "Ceci est une chaine"
character = "c"



if text[0].lower() == character:
	print("Votre chaine  commence par la lettre " + character)
else:
	print('Votre chaine ne commence pas par la lettre ' + character)
