import random

table = [[0 for _ in range(100)] for _ in range(100)]

for r, row in enumerate(table):
    for c in range(len(row)):
        if random.randint(1, 2) == 1:
            table[r][c] = 1