from collections import Counter, OrderedDict
from pprint import pprint
INPUT_PATH = 'data/day_6/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

DAYS = 256
input = input.split(',')
input = [int(i) for i in input if i != '']

counter = dict(Counter(input))
counter[-1] = 0
for i in range(0, 9):
    if i not in counter.keys():
        counter[i] = 0

for day in range(0, DAYS+1):
    summed = sum([v for k, v in counter.items() if k >= 0])
    print(dict(sorted(counter.items())))
    new_counter = counter.copy()

    for i in range(0, 9):
        new_counter[i-1] = counter[i]
    
    new_ones = new_counter[-1]
    new_counter[6] += new_ones
    new_counter[8] = new_ones

    counter = new_counter
print(day, summed)
