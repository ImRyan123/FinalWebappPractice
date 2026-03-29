import numpy as np

class Grid:
    def __init__(self, grid_y, grid_x):
        self.grid_y = grid_y
        self.grid_x = grid_x

        self.empty_cell = "#"

        self._make_grid()

    def _make_grid(self):
        # Make a 2D NumPy array filled with the empty cell symbol
        self.grid = np.full((self.grid_y, self.grid_x), self.empty_cell)

    def __str__(self):
        # Turn each NumPy row into a string, then join the rows with new lines
        return "\n".join(" ".join(row) for row in self.grid)


def main():
    grid = Grid(11, 11)
    print(grid)


if __name__ == "__main__":
    main()