import random

def create_grid(rows, cols, density):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if random.random() < density:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid


def count_alive_neighbors(grid, row, col):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if grid[i][j] == 1:
                count += 1

    if grid[row][col] == 1:
        count -= 1

    return count


def make_next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    next_grid = []
    for _ in range(rows):
        arr = []
        for _ in range(cols):
            arr.append(0)
        next_grid.append(arr)
    for i in range(rows):
        for j in range(cols):
            neighbors = count_alive_neighbors(grid, i, j)

            if grid[i][j] == 1:
                if neighbors == 2 or neighbors == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0
            else:
                if neighbors == 3:
                    next_grid[i][j] = 1
    return next_grid
