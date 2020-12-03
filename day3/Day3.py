# https://adventofcode.com/2020/day/3

file1 = open('input.txt', 'r')
Lines = file1.readlines()


def treeOnPathCounter(verticalMove, horizontalMove):
    treeCount = 0
    verticalLocation = 0
    horizontalLocation = 0
    while verticalLocation < len(Lines):
        line = Lines[verticalLocation].strip()
        if line[horizontalLocation] == '#':
            treeCount = treeCount + 1
            print("#: {}:{}".format(horizontalLocation, verticalLocation))
        else:
            print("O: {}:{}".format(horizontalLocation, verticalLocation))
        horizontalLocation = horizontalLocation + horizontalMove
        verticalLocation = verticalLocation + verticalMove
        if horizontalLocation >= len(line):
            # Max 31
            horizontalLocation = horizontalLocation - len(line)
            print("Reset horizontal move to:{}".format(horizontalLocation))
    print("Found trees: {}".format(treeCount))
    return treeCount


# Right 1, down 1. => 80
traverseOne = treeOnPathCounter(1, 1)
# Right 3, down 1. => 270
traverseTwo = treeOnPathCounter(1, 3)
# Right 5, down 1. => 60
traverseThree = treeOnPathCounter(1, 5)
# Right 7, down 1. => 63
traverseFour = treeOnPathCounter(1, 7)
# Right 1, down 2. => 26
traverseFive = treeOnPathCounter(2, 1)

solution = traverseOne * traverseTwo * traverseThree * traverseFour * \
           traverseFive

print("Solution:{}".format(solution))
