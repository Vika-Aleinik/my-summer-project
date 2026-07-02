from config import load_config
from logic import create_grid, make_next_generation
from ui import clear_screen, draw_grid
import time


config = load_config("config.txt")

rows = int(config.get("rows"))
cols = int(config.get("cols"))
density = float(config.get("density"))
delay = float(config.get("delay"))
alive = config.get("alive")
dead = config.get("dead")
separator = config.get("separator")

field = create_grid(rows, cols, density)
while True:
    clear_screen()
    draw_grid(field, alive, dead, separator)
    previous_field = field
    field = make_next_generation(field)
    time.sleep(delay)
    if field == previous_field:
        field = create_grid(rows, cols, density)
