import random

table = [[0 for _ in range(100)] for _ in range(100)]

for r, row in enumerate(table):
    for c in range(len(row)):
        if random.randint(1, 5) == 1:
            table[r][c] = 1


# table = [
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
#     [1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
#     [0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],


