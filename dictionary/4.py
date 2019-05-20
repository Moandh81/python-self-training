#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Write a Python script to check if a given key already exists in a dictionary.


keytotest =  input("Please input the key to test : \n")
counterTrue  = 0


dictionnaire = { 
                     'Gujarat' : 'Gandhinagar', 
                     'Maharashtra' : 'Mumbai', 
                     'Rajasthan' : 'Jaipur', 
                     'Bihar' : 'Patna'
                    } 





for key in dictionnaire:
	if key.lower() == keytotest.lower():
		counterTrue = counterTrue +1




if counterTrue == 1:
	print('This key exists in the dictionary')
else:
	print('This key does not exist in the dictionary')
