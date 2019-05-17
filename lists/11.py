#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Write a Python function that takes two lists and returns True if they have at least one common member.


liste1 = ["hello", "hi", "good evening"]

liste2 = ["good night", "good evening", "hi", "good night"]


for item in liste1:
	if item in liste2:
		print(item + " se trouve bien dans la liste 2")