import numpy as np
import os
import time

def clear():
    os.system("cls")

class Grid:

    def __init__(self, grid_y, grid_x):
        self.grid_y = grid_y
        self.grid_x = grid_x

        self.player_position = [self.grid_y // 2, self.grid_x // 2]

        self.empty_cell = "#"
        self.player_cell = "@"

        # Create NumPy grid filled with empty cells
        self.grid = np.full((self.grid_y, self.grid_x), self.empty_cell)

    def move_player(self, direction):
        dy, dx = direction

        new_y = self.player_position[0] + dy
        new_x = self.player_position[1] + dx

        if 0 <= new_y < self.grid_y and 0 <= new_x < self.grid_x:
            self.player_position = [new_y, new_x]
        else:
            print("ERROR")

    def render(self):
        # Reset grid to empty
        self.grid[:] = self.empty_cell

        # Place player at current position
        y, x = self.player_position
        self.grid[y, x] = self.player_cell

        return "\n".join("  ".join(row) for row in self.grid)


def main(delay):
    grid = Grid(11, 11)

    while True:
        print(grid.render())
        time.sleep(delay)

        # Move player up each frame
        grid.move_player((-1, 0))

        clear()


main(0.05)