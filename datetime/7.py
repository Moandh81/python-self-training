#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to print yesterday, today, tomorrow


from datetime import datetime, date, time 

today = datetime.today()

print("Today is " , today)




yesterday = today.timestamp() - 60*60*24

yesterday = date.fromtimestamp(yesterday)

print( "Yesterday is " , yesterday)




tomorrow = today.timestamp() + 60*60*24

tomorrow = date.fromtimestamp(tomorrow)

print("Tomorrow is ", tomorrow)