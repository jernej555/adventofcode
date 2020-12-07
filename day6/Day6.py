with open("input.txt") as f:
    lines = f.read()

groups = lines.split("\n\n")

atLeastOneTrue = 0
allTrue = 0
print("Task 1")
for group in groups:
    strip = group.replace('\n', '').strip()
    length = len(set(strip))
    atLeastOneTrue = atLeastOneTrue + length
    # print("Answers 1:{}".format(length))

print("Sum [at least one positive answer]: {}".format(atLeastOneTrue))

print("Task 2")
for group in groups:
    group_strip = group.strip()
    answerDictionary = {}
    personCount = 1
    for element in range(0, len(group_strip.strip())):
        answer = group_strip[element]
        if group_strip[element] == '\n':
            personCount = personCount + 1
        else:
            if answer in answerDictionary.keys():
                answerDictionary[answer] = answerDictionary[answer] + 1
            else:
                answerDictionary[answer] = 1
    print("Answers :{}".format(answerDictionary))
    print("Person count: {}".format(personCount))
    allTrue = allTrue + len([v for v in answerDictionary.values() if int(v) >= personCount])

print("Sum [all positive answers]: {}".format(allTrue))
