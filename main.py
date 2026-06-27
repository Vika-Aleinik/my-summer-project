from config import load_config
from logic import create_grid, make_next_generation
from ui import clear_screen, draw_grid
import time


config = load_config("config.txt")

rows = config.get("rows")
cols = config.get("cols")
density = config.get("density")
delay = config.get("delay")

field = create_grid(rows, cols, density)
while True:
    clear_screen()
    draw_grid(field)
    field = make_next_generation(field)
    time.sleep(delay)
