#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to find the second smallest largest in a list. 


sample = [1, 2, 3, 4, 5, 6]

print(max(sample))


sample.remove(max(sample))



print("The second smallet number in this list is {}".format(max(sample)))