file = open('input.txt', 'r')
Lines = file.readlines()


def codeToSeat(columnCode, up):
    fieldLength = 2 ** len(columnCode)
    min = 0
    max = fieldLength - 1
    for element in range(0, len(columnCode)):
        fieldLength = int(fieldLength / 2)
        if columnCode[element] == up:
            min = min + fieldLength
        else:
            max = max - fieldLength
        if fieldLength == 1:
            return max


maxSeatCode = 0
seatDictionary = {}
for line in Lines:
    seatCode = line.strip()
    row = codeToSeat(seatCode[0:7], 'B')
    column = codeToSeat(seatCode[7:11], 'R')
    seatCode = (row * 8) + column

    if row in seatDictionary.keys():
        seatDictionary[row].append(column)
        seatDictionary[row].sort()
    else:
        seatDictionary[row] = [column]
    print("Seat [{}:{}] =>code:{}".format(row, column, seatCode))

    if seatCode > maxSeatCode:
        maxSeatCode = seatCode

print("Max seat code:{}".format(maxSeatCode))

for key in seatDictionary:
    if len(seatDictionary[key]) < 8:
        print("Row: {} and seats: {}".format(key, seatDictionary.get(key)))
