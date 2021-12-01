INPUT_PATH = 'data/day_1/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.split('\n')
input = [int(i) for i in input[:-1]]  # empty line at the end of the file

counter = 0
for i, i_next in zip(input, input[1:]):
    if i_next > i:
        counter += 1
 
print(counter)