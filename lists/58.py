#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 58. Write a Python program to replace the last element in a list with another list. Go to the editor
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


list1 = [1, 3, 5, 7, 9, 10]
list2 =  [2, 4, 6, 8]

list1.remove(list1[len(list1) -1]) 


for item in list2:
 	list1.append(item)



print(list1) 