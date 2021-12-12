import numpy as np
from numpy.lib.function_base import _update_dim_sizes
INPUT_PATH = 'data/day_9/input.txt'


def check_input(x: int, y: int, arr) -> list:
    left = min(max(0,x-1), 99)
    right = min(max(0,x+1), 99)

    top = min(max(0,y-1), 99)
    bottom = min(max(0,y+1), 99)

    neighbours = {
        'left': arr[left, y],
        'right': arr[right, y],
        'top':  arr[x, top],
        'bottom': arr[x][bottom]
    }

    if x == left:
        del neighbours['left']
    if x == right:
        del neighbours['right']
    if y == top:
        del neighbours['top']
    if y == bottom:
        del neighbours['bottom']

    return list(neighbours.values())


with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.split('\n')
input = [line for line in input if line != '']

arr = [int(elem) for line in input for elem in line]
arr = np.array(arr).reshape(len(input), -1)

print(arr.shape)
minimums = []
for x in range(0, arr.shape[0]):
    for y in range(0, arr.shape[1]):
        elem = arr[x][y]
        neighbours = check_input(x, y, arr)
        if elem < min(neighbours):
            minimums.append(elem+1)

print(len(minimums))
print(sum(minimums))
