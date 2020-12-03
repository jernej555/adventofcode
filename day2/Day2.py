# https://adventofcode.com/2020/day/2
file1 = open('input.txt', 'r')
Lines = file1.readlines()

# Challenge one
# x = 0
# for line in Lines:
#     clearedLine = line.strip()
#     splitLine = clearedLine.split(" ")
#     limit = splitLine[0].split("-")
#     minCount = int(limit[0])
#     maxCount = int(limit[1])
#     char = splitLine[1][:-1]
#     passwordToCheck = splitLine[2]
#
#     counter = passwordToCheck.count(char)
#     if counter < minCount or counter > maxCount:
#         print("Min: {}, Max: {}, Of: {}, textToClean:{}".format(minCount, maxCount, char, passwordToCheck))
#     else:
#         x = x + 1
# print("Valid password count: {}".format(x))

# Challenge two
x = 0
for line in Lines:
    clearedLine = line.strip()
    splitLine = clearedLine.split(" ")
    limit = splitLine[0].split("-")
    minCount = int(limit[0])
    maxCount = int(limit[1])
    char = splitLine[1][:-1]
    passwordToCheck = splitLine[2]

    checkCount = 0

    if passwordToCheck[minCount - 1] == char:
        checkCount += 1

    if maxCount - 1 <= len(passwordToCheck) and passwordToCheck[maxCount - 1] == char:
        checkCount += 1

    if checkCount != 1:
        print("Min: {}, Max: {}, Of: {}, password:{}".format(minCount, maxCount, char, passwordToCheck))
    else:
        x = x + 1

print("Valid password count: {}".format(x))
