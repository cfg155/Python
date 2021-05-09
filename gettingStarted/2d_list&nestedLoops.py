num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(num_grid[3][0])
"""
    Read by row x column and it starts from index 0
    num_grid[3][0] means row index 3 and column index 0
"""

for row in num_grid:
    for col in row:
        print(col)
