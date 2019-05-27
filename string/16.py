#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python function to insert a string in the middle of a string.
# Sample function and result : 
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}





def insert_string_middle(word1, word2):
	print(word1[:len(word1)//2 ] + word2 + word1[len(word1)//2:])


insert_string_middle('{{}}', 'PHP')