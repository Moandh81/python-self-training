#!/usr/bin/env python
# -*- coding: utf-8 -*-



# Write a Python function to create the HTML string with tags around the word(s)
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'


txt = "This is a sample tag"

def add_tags(tag, text):
	return "<" + tag + ">" + text + "</"+ tag +">"


print(add_tags("p", txt))
print(add_tags("div", txt))