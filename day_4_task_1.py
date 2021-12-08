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

rows_and_cols = []
for m in matrices:
    rows = [row for row in m]
    cols= []
    for n in range(0, len(rows)):
        col = [r[n] for r in rows]
        cols.append(col)
    rows_and_cols.append([rows, cols])

done = False
i = 5
while not done:
    numbers_vector = set(numbers[:i])
    for row_col in rows_and_cols:
        rows = row_col[0]
        cols = row_col[1]
        for r in rows:
            if set(r).issubset(numbers_vector):
                print(f'{r} is in')
                for print_row in rows:
                    print(print_row)
                done = True
                elements = [elem for row in rows for elem in row]
                unmarked = [e for e in elements if e not in numbers_vector]
                unmaked_sum = sum(unmarked)
                last_number = numbers[i-1]
                final_score = unmaked_sum * last_number
        for c in cols:
            if set(c).issubset(numbers_vector):
                print(f'{c} is in')
                for print_row in rows:
                    print(print_row)
                done = True
                elements = [elem for col in cols for elem in col]
                unmarked = [e for e in elements if e not in numbers_vector]
                unmaked_sum = sum(unmarked)
                last_number = numbers[i-1]
                final_score = unmaked_sum * last_number
    i += 1

print(final_score)