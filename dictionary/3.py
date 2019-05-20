#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python script to concatenate following dictionaries to create a new one

# Sample Dictionary : 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}



dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dictionnaire = {}


for key, value in dic1.items():
	dictionnaire[key] = value


for key, value in dic2.items():
	dictionnaire[key] = value


for key, value in dic3.items():
	dictionnaire[key] = value



print(dictionnaire)