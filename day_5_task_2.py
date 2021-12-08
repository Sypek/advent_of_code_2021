from collections import Counter

INPUT_PATH = 'data/day_5/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.split('\n')
input = [i for i in input if i != '']


arr = []
for line in input:
    coords1, coords2 = line.split(' -> ')
    x1, y1 = coords1.split(',')
    x2, y2 = coords2.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            arr.append(str(x1) + ',' +  str(y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            arr.append(str(x) + ',' + str(y1))
    else:  # diagonals
        x_delta = x2 - x1
        y_delta = y2 - y1
        delta = abs(x_delta)
        if x_delta > 0 and y_delta > 0:
            for x in range(delta+1):
                arr.append(str(x1 + x) + ',' + str(y1 + x))
        elif x_delta > 0 and y_delta < 0:
            for x in range(delta+1):
                arr.append(str(x1 + x) + ',' + str(y1 - x))
        elif x_delta < 0 and y_delta > 0:
            for x in range(delta+1):
                arr.append(str(x1 - x) + ',' + str(y1 + x))
        elif x_delta < 0 and y_delta < 0:
            for x in range(delta+1):
                arr.append(str(x1 - x) + ',' + str(y1 - x))

counter = Counter(arr)

count = [k for k, v in counter.items() if v >=2]
print(len(count)) 