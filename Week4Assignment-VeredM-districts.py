#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wellstone
ME 106
Week 4 Assginment
Part IIB

Created on Sat Aug 11 12:59:47 2018

@author: mvered
"""

districts = [['SD',5],
             ['HD',11],
             ['CD',4]]

districtList = []

for districtType in districts:
    numberDistricts = districtType[1]
    for x in range(1,numberDistricts+1):
        entry = districtType[0] + str(x)
        districtList.append(entry)

separator = ", "
districtJoinedList = separator.join(districtList)

print(districtJoinedList)