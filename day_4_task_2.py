INPUT_PATH = 'data/day_4/input.txt'

with open(INPUT_PATH, 'r') as f:
    input = f.read()

input = input.split('\n\n')
input = [i for i in input if i != '']
 
numbers = input[0]
numbers = [int(i) for i in numbers.split(',')]

matrices = []

for i in input[1:]:
    matrix = []
    rows = i.split('\n')
    for row in rows:
        entries = [int(j) for j in row.split()]
        if len(entries) == 5:
            matrix.append(entries)
    matrices.append(matrix)

rows_and_cols = {}
for m_idx, m in enumerate(matrices):
    rows = [row for row in m]
    cols= []
    for n in range(0, len(rows)):
        col = [r[n] for r in rows]
        cols.append(col)
    rows_and_cols[m_idx] = [rows, cols]

done = False
i = 5
N_matrices = len(matrices)
COUNTER = set()

while N_matrices - len(COUNTER) > 0:
    if N_matrices - len(COUNTER) == 1:
        last_matrix_idx = set(rows_and_cols.keys()).difference(COUNTER)
        last_matrix_idx = list(last_matrix_idx)[0]
        print('Last matrix idx:', last_matrix_idx)
    numbers_vector = set(numbers[:i])
    for idx, row_col in rows_and_cols.items():
        rows = row_col[0]
        cols = row_col[1]
        for r, c in zip(rows, cols):
            if set(r).issubset(numbers_vector) or set(c).issubset(numbers_vector) :
                COUNTER.add(idx)

    i += 1

last_number = numbers[i-2]

cols = rows_and_cols[last_matrix_idx][1]
elements = [elem for col in cols for elem in col]
unmarked = [e for e in elements if e not in numbers_vector]
unmaked_sum = sum(unmarked)
final_score = unmaked_sum * last_number
print(f'unmarked sum: {unmaked_sum}, last_number: {last_number}')
print(final_score)