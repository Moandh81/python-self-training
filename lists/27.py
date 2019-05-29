#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to find the second smallest number in a list. 


sample = [1, 2, 3, 4, 5, 6]

print(min(sample))


sample.remove(min(sample))



print("The second smallet number in this list is {}".format(min(sample)))