#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python script to merge two Python dictionaries.


dict1 = {
	
"name" : "john" ,
"age" : 33 ,
"email" : "john@john.com"

}

dict2 = {
	
"hobbies" : ["trekking", "walking", "cycling"],
"car_brand" : "Ford",
"model" : "Fiesta"

}

merged = {}


for key, value in dict1.items():
	merged[key] = value


for key, value in dict2.items():
	merged[key] = value


print(merged)