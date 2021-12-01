INPUT_PATH = 'data/day_1/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.split('\n')
input = [int(i) for i in input[:-1]]  # empty line at the end of the file

previous_sum = 0
counter = 0
iter = 0

for i, j, k in zip(input, input[1:], input[2:]):
    current_sum = i + j + k
    if current_sum > previous_sum and iter > 0:
        counter += 1
    previous_sum = current_sum
    iter += 1

print(counter)