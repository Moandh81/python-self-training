#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Write a Python program to calculate a number of days between two dates.

from datetime import date



t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)
