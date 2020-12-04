# https://adventofcode.com/2020/day/4#part2
import re

with open("input.txt") as f:
    lines = f.read()

passports = lines.split("\n\n")


def propertyCheck(passportProperties):
    isValid = True
    for property in passportProperties:
        split = property.split(":")
        if split[0] == "byr":
            isValid = yearCheck(split[1], 4, 1920, 2002, "byr")
        if split[0] == "iyr":
            isValid = yearCheck(split[1], 4, 2010, 2020, "iyr")
        if split[0] == "eyr":
            isValid = yearCheck(split[1], 4, 2020, 2030, "eyr")
        if split[0] == "hgt":
            isValid = hgtCheck(split[1])
        if split[0] == "hcl":
            isValid = hclCheck(split[1])
        if split[0] == "ecl":
            isValid = eclCheck(split[1])
        if split[0] == "pid":
            isValid = pidCheck(split[1])
        if not isValid:
            return False
    return isValid


def yearCheck(input, digits, minYear, maxYear, typeOfCheck):
    if (len(input) > digits):
        print("Invalid year ({}) length: {}".format(typeOfCheck, input))
        return False
    numCheck = int(input)
    if numCheck < minYear or numCheck > maxYear:
        print("Invalid year ({}) length: {}".format(typeOfCheck,numCheck))
        return False
    return True


def hgtCheck(input):
    split = re.split('(\d+)', input.strip())
    size = int(split[1])
    metric = split[2]
    if metric == "cm":
        return 150 <= size <= 193
    if metric == "in":
        return 59 <= size <= 76
    print("Invalid hgt: {} {}".format(size, metric))
    return False


def hclCheck(input):
    pattern = re.compile("^[#][0-9a-f]{6}$")
    match = pattern.match(input)
    if not match:
        print("Invalid hcl: {}".format(input))
    return match


def eclCheck(input):
    contains = input in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if not contains:
        print("Invalid ecl: {}".format(input))
    return contains


def pidCheck(input):
    if len(input) != 9:
        print("Invalid pid: {}".format(input))
        return False
    return True


# CID
requiredFieldCount = 0
validPassportCount = 0
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for passport in passports:
    if all(x in passport for x in requiredFields):
        requiredFieldCount += 1
        passportProperties = passport.split()
        if propertyCheck(passportProperties):
            print("Valid passports")
            validPassportCount += 1
        else:
            print("Invalid passport")

print("Required fields count: {}".format(requiredFieldCount))
print("Valid count: {}".format(validPassportCount))
