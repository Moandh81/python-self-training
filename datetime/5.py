#!/usr/bin/env python
# -*- coding: utf-8 -*-




# Write a Python program to subtract five days from current date.
# Sample Date : 
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17



from datetime import date, datetime

a = datetime.today()



newdate = date.fromtimestamp(a.timestamp() - 5*24*60*60)


print(newdate)

