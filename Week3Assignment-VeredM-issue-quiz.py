
# -*- coding: utf-8 -*-
"""
Week 3 Assignment - Wellstone ME 106 - Part I
@author: mvered
"""

score = 50

startMessage = "Welcome to the public lands quiz. Please enter 'T' for true and 'F' for false."
endMessage = "You have finished the quiz. Your score is: "
okayMessage = "Your answer has been recorded."
errorMessage = "I didn't catch that. For future quesitons, please enter either 'T' for true or 'F' for false."

print(startMessage)

q1 = input('I support preserving existing Wilderness Study Area designations. ')
if q1 == 'T' or 't':
    score = score + 10
    print(okayMessage)
elif q1 == 'F' or 'f':
    score = score - 10
    print(okayMessage)
else:
    print(errorMessage)

q2 = input('I support increasing opportunities for motorized recreation, such as snow-mobiling, on our public lands. ')
if q2 == 'T':
    score = score - 10
    print(okayMessage)
elif q2 == 'F':
    score = score + 10
    print(okayMessage)
else:
    print(errorMessage)

q3 = input('I take action to preserve public lands, such as by calling my representatives, donating to conservation organizations, or volunteering with a trail crew. ')
if q3 == 'T':
    score = score + 10
    print(okayMessage)
elif q3 == 'F':
    score = score - 10
    print(okayMessage)
else:
    print(errorMessage)

q4 = input('I believe we should consider transferring some of our existing public lands to private ownership. ')
if q4 == 'T':
    score = score - 10
    print(okayMessage)
elif q4 == 'F':
    score = score + 10
    print(okayMessage)
else:
    print(errorMessage)

q5 = input('I believe it should be easier for companies to get permission to do natural resource extraction (mining, logging, etc) on our public lands. ')
if q5 == 'T':
    score = score - 10
    print(okayMessage)
elif q5 == 'F':
    score = score + 10
    print(okayMessage)
else:
    print(errorMessage)

print(endMessage + str(score))

if score > 85:
    print('Congratulations! You are a strong supporter of our public lands!')
elif (score > 65) and (score < 85):
    print('You are a pretty good public lands supporter, but you can still do more. ')
elif (score > 35) and (score < 65):
    print('Our public lands are an important resource for our outdoor recreation economy and the enjoyment of future generations. Consider learning more about their importance. ')
else:
    print('You are anti public lands. Boo! ')
