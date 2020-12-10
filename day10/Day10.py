lines = []
for line in open("input.txt"):
    lines.append(int(line))

n = len(lines)
lines.append(0)
lines.sort()
lines.append(lines[n] + 3)

differenceDictionary = {}
for i in range(1, len(lines)):
    joltDiff = lines[i] - lines[i - 1]
    if joltDiff in differenceDictionary:
        differenceDictionary[joltDiff] = differenceDictionary[joltDiff] + 1
    else:
        differenceDictionary[joltDiff] = 1

print(differenceDictionary)

arrangements = [1]
for i in range(1, len(lines)):
    arrange = arrangements[i - 1]
    j = i - 2
    while j >= 0 and lines[i] - lines[j] <= 3:
        arrange += arrangements[j]
        j -= 1

    arrangements.append(arrange)

print(f"There are {arrangements[-1]} valid arrangements")
