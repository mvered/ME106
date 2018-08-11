#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Week 3 Assignment - Wellstone ME 106 - Part II

Created on Sat Aug 11 12:46:54 2018

@author: mvered
"""

countdownMessage = ' more days until the election!'
lastDayMessage = ' more day until the election!'
electionDayMessage = 'Today is election day!'

daysLeft = input('How many days are left until election day? ')
daysLeft = int(daysLeft)

while daysLeft > 1:
    print(str(daysLeft) + countdownMessage)
    daysLeft = daysLeft - 1

print(str(daysLeft) + lastDayMessage)

print(electionDayMessage)