''' Week 2 Assignment
by Michelle Vered
'''

# Part A
print("Part A")

supporter = ["Charley", "Bordelon West", "St Josephine", "LA", "Iberia", "70563", True]
answerA1 = supporter[0]
print("1. " + answerA1)

answerA2 = supporter[2]
print("2. " + answerA2)

answerA3 = supporter[-1]
print("3. " + str(answerA3))

answerA4 = supporter[2:5]
print("4. " + str(answerA4))

answerA5 = supporter[4:7]
print("5. " + str(answerA5))

answerA6 = [supporter[0], supporter[4], supporter[5], supporter[6]]
print("6. " + str(answerA6))

answerA7 = str(supporter[0]) + " " + str(supporter[1]) + ": " + str(supporter[2]) + ", " + str(supporter[3]) + " " + str(supporter[5])
print("7. " + str(answerA7))

answerA8_part1 = supporter[2].split()
answerA8_part2 = supporter[1].split()
answerA8 = answerA8_part1[1] + " " + answerA8_part2[1]
print("8. " + str(answerA8))

#Part B
print("Part B")

# 1
firstName = "akilah"
firstName = firstName.upper()
print("1. " + firstName)

# 2
firstName = "     kemi     "
firstName = firstName.strip()
print("2. " + firstName)

# 3
cities = "Mesa0Tucson0Yuma0Tuba City"
Cities = cities.split('0')
print("3. " + str(Cities))

# 4
rallyStart = "4pm et"
rallyStart = rallyStart.upper()
print("4. " + rallyStart)

# 5
senateDistrict = "SD42xxxxxxx"
senateDistrict = senateDistrict.rstrip('x')
print("5. " + senateDistrict)

# 6
chant = "Chant down Bablyon, grassroots is the bomb"
chant = chant.upper()
print("6. " + chant)

# 7
emailSuffix = "aliyaonthedecks@gmail.com"
emailSuffix = emailSuffix.split('@')[1]
print("7. " + emailSuffix)

# 8
fullName = "Alexandria Ocasio Cortez"
fullNameList = fullName.split()
fullName = fullNameList[1].upper() + "-" + fullNameList[2].upper() + ", " + fullNameList[0]
print("8. " + fullName)

# 9
street = "1207NLaSalleBlvd"
street = street[0:4] + " " + street[5:7] + " " + street[7:12] + " " + street[12:]
print("9. " + street)

# 10
daytimePhone = "5137782390"
daytimePhone = "(" + daytimePhone[0:3] + ") " + daytimePhone[3:6] + "-" + daytimePhone[6:10]
print("10. " + daytimePhone)



