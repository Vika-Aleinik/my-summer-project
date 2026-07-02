import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def draw_grid(grid, alive_cell_symbol, dead_cell_symbol, separator):
    for row in grid:
        line = []
        for cell in row:
            if cell == 1:
                line.append(alive_cell_symbol)
            elif cell == 0:
                line.append(dead_cell_symbol)
            else:
                print("Error")

        print(separator.join(line))
