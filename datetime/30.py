#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to convert a date to the timestamp.


from datetime import datetime


now = datetime.now()

timestamp = datetime.timestamp(now)

print(timestamp)