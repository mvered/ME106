#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:12:39 2018

@author: mvered

Week 6 Assignment 
Wellstone ME 106
"""

import pandas as pd

# a. Reads volunteer.csv and saves as dataframe
df = pd.read_csv('volunteer.csv')

# b. Renames columns 'Phone 1' and 'Phone 2'
df.rename(inplace = True, columns = {'Phone 1': 'Daytime phone', 'Phone 2':'Evening phone'})

# c. Prints out first & last name & daytime phone for first 20 records
print('First and last name and daytime phone for first 20 records')
print(df.loc[0:20, ['First Name','Last Name', 'Daytime phone']])

# d. Counts how many times each zip code appears & saves counts as new df
dataValues = df['Zip5'].value_counts()
dfCounts = pd.DataFrame(df['Zip5'].value_counts())
dfCounts.index.name = 'zipcode'
dfCounts.rename(inplace=True, columns = {'Zip5': 'count'})

# e. Write the zipcode counts to a new csv
csv = 'zip5_counts.csv'
dfCounts.to_csv(csv)

# f. Have your script peform one other pandas operation of your choice
# replaces empty values in the donation amount column with 0
df.fillna(value = {'Total Donation Amount':0}, inplace=True)
df.to_csv('volunteer-updated.csv')