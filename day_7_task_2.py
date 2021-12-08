INPUT_PATH = 'data/day_7/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.split(',')
input = [int(i) for i in input if i != '']  # empty line at the end of the file

minimum = min(input)
maximum = max(input)

def sum_from_1_to_n(n: int) -> int:
    return sum([i for i in range(1, n+1)])

assert sum_from_1_to_n(1) == 1
assert sum_from_1_to_n(0) == 0
assert sum_from_1_to_n(4) == 10

min_distance = 0
for i in range(minimum, maximum):
    distances = [abs(val - i) for val in input]
    distance = sum([sum_from_1_to_n(dist) for dist in distances])
    if distance < min_distance or min_distance == 0:
        min_distance = distance

print(min_distance)