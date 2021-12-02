INPUT_PATH = 'data/day_2/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.split('\n')
input = [i for i in input if i != '']

x_position = 0
y_position = 0
for row in input:
    direction, magnitude = row.split(' ')

    if direction == 'forward':
        x_position += int(magnitude)
    elif direction == 'up':
        y_position -= int(magnitude)
    elif direction == 'down':
        y_position += int(magnitude)

print(f'x poxistion (horizontal) = {x_position}')
print(f'y position (vertical, depth) = {y_position}')
print(f'multiplication = {x_position * y_position}')