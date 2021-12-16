from collections import Counter
import tqdm
INPUT_PATH = 'data/day_14/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

template, rules = input.split('\n\n')
rules = [i for i in rules.split('\n') if i != '']
rules = {r.split(' -> ')[0]: r.split(' -> ')[1] for r in rules}

N_STEPS = 10
print(f'TEMPALTE: {template}')
for step in tqdm.tqdm(range(N_STEPS)):
    new_str = template[0]
    for counter, (first, second) in enumerate(zip(template, template[1:])):
        element = first + second
        insert = rules[element] + second
        new_str += insert
    template = new_str
    # print(f'After step {step+1}: {template}')

min = min(Counter(template).values())
max = max(Counter(template).values())

print(max - min)