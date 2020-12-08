file = open('input.txt', 'r')
Lines = file.readlines()


def runProgramPart1(lines):
    visitedLines = set()
    lineIndex = 0
    accumulator = 0
    while True:
        if lineIndex == 601:
            print("Reached end line {} with value: {}".format(lineIndex, line))
            print("Accumulator value: {}".format(accumulator))
            break
        line = lines[lineIndex].split(" ")
        if lineIndex in visitedLines:
            print("Line: {} already visited with value: {}".format(lineIndex, line))
            print("Accumulator value: {}".format(accumulator))
            break
        if line[0] == "nop":
            visitedLines.add(lineIndex)
            lineIndex = lineIndex + 1
        if line[0] == "acc":
            visitedLines.add(lineIndex)
            lineIndex = lineIndex + 1
            if line[1][0] == "+":
                accumulator = accumulator + int(line[1][1:])
            if line[1][0] == "-":
                accumulator = accumulator - int(line[1][1:])
        if line[0] == "jmp":
            visitedLines.add(lineIndex)
            if line[1][0] == "+":
                lineIndex = lineIndex + int(line[1][1:])
            if line[1][0] == "-":
                lineIndex = lineIndex - int(line[1][1:])
            if lineIndex == 601:
                print("Reached end line {} with value: {}".format(lineIndex, line))
                print("Accumulator value: {}".format(accumulator))
                break


def runProgramPart2(lines):
    changedLines = set()
    visitedLines = set()
    lineIndex = 0
    accumulator = 0
    simulationRunning = False
    while True:
        if lineIndex == 601:
            print("Reached end line {} with value: {}".format(lineIndex, line))
            print("Accumulator value: {}".format(accumulator))
            break
        line = lines[lineIndex].split(" ")
        if lineIndex in visitedLines:
            print("Line: {} already visited with value: {}".format(lineIndex, line))
            visitedLines = set()
            lineIndex = 0
            simulationRunning = False
        if line[0] == "acc":
            visitedLines.add(lineIndex)
            lineIndex = lineIndex + 1
            if line[1][0] == "+":
                accumulator = accumulator + int(line[1][1:])
            if line[1][0] == "-":
                accumulator = accumulator - int(line[1][1:])
        if line[0] == "jmp":
            if lineIndex not in changedLines and not simulationRunning:
                changedLines.add(lineIndex)
                simulationRunning = True
                print("Updated line index: {}: from: {}", lineIndex, line)
                line[0] = "nop"
            else:
                visitedLines.add(lineIndex)
                if line[1][0] == "+":
                    lineIndex = lineIndex + int(line[1][1:])
                if line[1][0] == "-":
                    lineIndex = lineIndex - int(line[1][1:])
        if line[0] == "nop":
            visitedLines.add(lineIndex)
            lineIndex = lineIndex + 1


# Part 1
#runProgramPart1(Lines)

# Part 2
runProgramPart2(Lines)
# We need to edit instruction in line 193 ['jmp', '+174\n']
