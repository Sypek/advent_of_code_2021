import numpy as np
import re
INPUT_PATH = 'data/day_13/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.splitlines()
input = [i for i in input if i != '']
folds = []
coordinates = []
for i in input:
    if i[0] == 'f':
        folds.append(i)
    else:
        coordinates.append(i)

folds = [re.search(r"[xy]=[0-9]*", i).group(0) for i in folds]
folds = [i.split('=') for i in folds]
folds = [[i[0], int(i[1])] for i in folds]
print(folds)

max_x = 0
max_y = 0
int_coords = []
for i in coordinates:
    x, y = i.split(',')
    x = int(x)
    y = int(y)

    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    int_coords.append((x, y))
print(max_x, max_y)

print('First coordinates: ', int_coords[0])
print('Last coordinates: ', int_coords[-1])

arr = np.zeros(shape=(max_x+1, max_y+1))
for coords in int_coords:
    x, y = coords
    arr[x][y] = 1

print(arr.shape)
print(arr.sum())

# print('First fold: ', fol)
x_fold = 655

for x in range(x_fold+1, arr.shape[0]):
    for y in range(0, arr.shape[1]):
        x_mirror = arr.shape[0] - x - 1
        if arr[x][y] > 0:
            arr[x_mirror][y] +=1

# limit array after fold
arr = arr[:x_fold, :]
print(arr.shape)
print((arr>0).sum())

