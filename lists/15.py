#!/usr/bin/env python
# -*- coding: utf-8 -*-

 # Write a Python program to shuffle and print a specified list.


import random

number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]


print ("Original list : ",  number_list)

random.shuffle(number_list) 

print ("List after first shuffle  : ",  number_list)

