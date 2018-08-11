#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wellstone
ME 106
Week 4 Assginment
Part I

Created on Sat Aug 11 12:59:21 2018

@author: mvered

"""

# list format: [item name, number needed, number owned, number checked out]

equipmentCheckout = [['Megaphone', 6, 3, 3],
                     ['SM generator',4,6,2],
                     ['LG generator',2,0,0],
                     ['Gas mask - SM',4,2,1],
                     ['Tent - 2 person',6,4,4],
                     ['Gas mask - MD',4,0,0],
                     ['Blankets',30,12,12],
                     ['Gas mask - LG',4,3,3],
                     ['Gas mask - XL',4,6,4]]

# count number of items you still need
neededItems = 0
for item in equipmentCheckout:
    neededItems = neededItems + item[1]

# count number of surplus items we have that are not checked out
surplusItems = 0
for item in equipmentCheckout:
    surplusItems = surplusItems + item[2] - item[3]

# count number of gas masks you own that are not checked out
# note: write code that refers to gas mask by name, not index number
gasMasks = 0
for item in equipmentCheckout:
    if item[0][0:8] == 'Gas mask':
        gasMasks = gasMasks + item[2] - item[3]
    else:
        gasMasks = gasMasks

# report the results of these counts using print statements
print('The number of items still needed is: ' + str(neededItems))
print('The number of surplus items we have is: ' + str(surplusItems))
print('The number of gas masks we own that are not checked out is: ' + str(gasMasks))