file = open('input.txt', 'r')
Lines = file.readlines()


def findInvalidLine(lines, windowSize):
    windowsStart = 0
    currentElement = windowSize
    while currentElement < len(lines):
        sumDetected = False
        for i in range(windowsStart, currentElement - 1):
            for j in range(i + 1, currentElement):
                currentVal = int(lines[currentElement])
                currentSum = int(lines[i]) + int(lines[j])
                print("Current val: {}, current sum: {}".format(currentVal, currentSum))
                if currentVal == currentSum:
                    print("Element at position: {} is valid".format(currentElement))
                    windowsStart = windowsStart + 1
                    currentElement = currentElement + 1
                    sumDetected = True
                    break
        if not sumDetected:
            print("Element: {} at position: {} is not valid".format(lines[currentElement], currentElement))
            # windowsStart = windowsStart + 1
            # currentElement = currentElement + 1
            break


def findSumUp(lines, number):
    windowsStart = 0
    for i in range(windowsStart, len(Lines) - 1):
        sum = 0
        for j in range(i + 1, len(Lines)):
            sum = sum + int(lines[j])
            if sum == number and j - i > 1:
                print("Detected set between: {} and {}".format(i, j))
                minAndMax = [int(i) for i in lines[i:j]]
                print("Sum: {}".format(min(minAndMax) + max(minAndMax)))


# Part 1
# findInvalidLine(Lines, 25)
# Invalid number 167829540

# Part 2
findSumUp(Lines, 167829540)
# Sum of min and max number: 28045630
