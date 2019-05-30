#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to get the current time in Python.
# Sample Format :  13:19:49.078205



from datetime import datetime

now = datetime.now()

now = now.strftime("%H:%M:%S.%f")


print(now)
