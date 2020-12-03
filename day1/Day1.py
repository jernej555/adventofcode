# https://adventofcode.com/2020/day/1
import time

file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character

def naiveSolution():
    start_time = time.time()
    for line in Lines:
        for secondLine in Lines:
            firstNum = int(line.strip())
            secondNum = int(secondLine.strip())
            if firstNum + secondNum == 2020:
                print("First number: {} Second number: {}".format(firstNum, secondNum))
                return time.time() - start_time
    return time.time() - start_time

def mapSolution():
    # https://coderbyte.com/algorithm/two-sum-problem
    start_time = time.time()
    map = {}
    for line in Lines:
        num = int(line.strip())
        diff = 2020 - num
        if (diff in map.keys()):
            print("First number: {} Second number: {}".format(num, diff))
            break
        else:
            map[num] = diff
    return time.time() - start_time

print("--- Naive solution: %s seconds ---" % naiveSolution())
print("--- Map solution: %s seconds ---" % mapSolution())
