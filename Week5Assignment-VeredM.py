#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Week 5 Assignment Wellstone ME 106

Created on Thu Aug 16 20:12:37 2018

@author: mvered

Assignment: Using read_csv

"""
person = {"EID":2907071,
          "Last Name": "Colvin",
          "First Name": "Claudette",
          "Address": "588 Example St.",
          "City": "Montgomery",
          "State": "AL",
          "Zip5": 36108,
          "Email 1": "claudette.colvin43@example.com",
          "Email 2": "",
          "Phone 1": "3342423935",
          "Phone 2": "3345555934",
          "Volunteer": True,
          "Precinct Captain": True}

#Part I 
"""

1. What are the keys in this dictionary?
Keys in this dictionary are 
EID
Last Name
First Name 
Address
City
State
Zip5
Email 1
Email 2
Phone 1 
Phone 2 
Volunteer
Precinct Captain

2. What will the following return?
a. person["Address"] 
588 Example St.
b. person["Volunteer"]
True
c. person[Email 1]
SyntaxError
d. person["Phone 2"]
3345555934
e. person['Phone 2']
3345555934
f. person."Zip5"
SyntaxError
g. person.Zip5
SyntaxError
h. person["Phone 1"][0:2]
33

"""

#Part II
countRecords = 0
countVols = 0
countDonors = 0
volList = [['First Name','Last Name','City','State','Email 1',\
            'Email 2','Phone']]

import csv

with open('volunteer.csv','r') as volunteer_file:
    csv_reader = csv.reader(volunteer_file)
    for row in csv_reader:
        countRecords += 1
        if row[11] == 'Yes':
            countDonors += 1
        if row[9] == 'Yes':
            countVols += 1
            volRecord = [row[2],row[1],row[4],row[5],row[7],\
                             row[8],row[13]]
            volList.append(volRecord)

    
print("Number of people on list: " + str(countRecords))
print("Number of volunteers: " + str(countVols))
print("Number of donors: " + str(countDonors))

#print("Volunteer list: " + ', '.join(volList))

#Part III
with open('volunteer-export.csv','w') as new_file:
    csv_writer = csv.writer(new_file, delimiter=',')
    for item in volList:
        csv_writer.writerow(item)


#Part IV
choice1 = input('Enter A for a list of all volunteers or B for a subset of volunteers: ')

countVols2 = 0
volList2 = [['First Name','Last Name','City','State','Email 1',\
            'Email 2','Phone']]
volList3 = [['First Name','Last Name','City','State','Email 1',\
            'Email 2','Phone']]

with open('volunteer.csv','r') as volunteer_file2:
    csv_reader2 = csv.DictReader(volunteer_file2)
    for row in csv_reader2:
        if row['Volunteer'] == 'Yes':
            countVols2 += 1
            volRecord2 = [row['First Name'],row['Last Name'], \
                         row['City'],row['State'],row['Email 1'],\
                             row['Email 2'],row['Phone 1']]
            volList2.append(volRecord2)

if choice1 == 'A':
    with open('volunteer-export-userchoice.csv','w') as export_file:
        csv_writer = csv.writer(export_file, delimiter=',')
        for item in volList2:
            csv_writer.writerow(item)
elif choice1 == 'B':
    choice2 = input('Please enter a letter and you will receive \
                    an export containing a list of volunteers \
                    whose last name begins with that letter: ')
    choice2Lower = choice2.lower()
    for record in volList2:
        if (record[1][0] == choice2) or (record[1][0] == choice2Lower):
            volList3.append(record)
    
    with open('volunteer-export-userchoice.csv','w') as export_file:
        csv_writer = csv.writer(export_file, delimiter=',')
        for item in volList3:
            csv_writer.writerow(item)
else:
    print('Error: Your input was not recognized.')
    