#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wellstone
ME 106
Week 4 Assginment
Part IIA

Created on Sat Aug 11 13:00:05 2018

@author: mvered
"""
#Note: Data shows number of signatures collected by each of five team members working on a ballot initiative.
#Team uses "-1" to indicate that someone did not work that day.
weeklyReport = [['Monday',[30,45,-1,18,20]],
                ['Tuesday',[12,40,-1,19,34]],
                ['Wednesday',[22,25,31,36,-1]],
                ['Thursday',[-1,28,39,22,-1]],
                ['Friday',[-1,25,24,0,2]],
                ['Saturday',[38,-1,73,-1,50]],
                ['Sunday',[64,-1,44,-1,61]]
                ]

#write a program using nested loops
#total number of signatures collected for the week
signaturesTotal = 0
for day in weeklyReport:
    for employee in day[1]:
        if employee == -1:
            signaturesTotal = signaturesTotal
        else:
            signaturesTotal = signaturesTotal + employee

print('Total signatures collected: ' + str(signaturesTotal))

#name of the day on which your team collected the most signatures
signaturesDaily = 0
dailyTotals = []
for day in weeklyReport:
    for employee in day[1]:
          if employee == -1:
            signaturesDaily = signaturesDaily
          else:
            signaturesDaily = signaturesDaily + employee
    dailyTotals.append([day[0],signaturesDaily])
    signaturesDaily = 0

maxSignatures = [dailyTotals[0][0],dailyTotals[0][1]]
for day in dailyTotals[1:7]:
    if day[1] > maxSignatures[1]:
        maxSignatures = [day[0],day[1]]
    else:
        maxSignatures = maxSignatures
       
print('The most signatures were collected on: ' + str(maxSignatures[0]))
 

#name of the day on which your team collected the least signatures
minSignatures = [dailyTotals[0][0],dailyTotals[0][1]]
for day in dailyTotals[1:7]:
    if day[1] < minSignatures[1]:
        minSignatures = [day[0],day[1]]
    else:
        minSignatures = minSignatures
       
print('The least signatures were collected on: ' + str(minSignatures[0]))

