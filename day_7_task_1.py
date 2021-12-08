INPUT_PATH = 'data/day_7/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.split(',')
input = [int(i) for i in input if i != '']  # empty line at the end of the file

minimum = min(input)
maximum = max(input)

min_distance = 0
for i in range(minimum, maximum):
    distance = sum[abs(val - i) for val in input]
    if distance < min_distance or min_distance == 0:
        min_distance = distance

print(min_distance)