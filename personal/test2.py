import time
import os

class Grid:
    
    def __init__(self, grid_y, grid_x):
        self.grid_y = grid_y
        self.grid_x = grid_x
        self.loading_cycle = [
            "-",
            "/",
            "|",
            "\\"
        ]
        
        self.empty_cell = " "
        self.grid = []
    
    def _make_grid(self):
        self.grid = []
        for _ in range(self.grid_y):
            self.grid.append([self.empty_cell for _ in range(self.grid_x)])
        
    def load(self):
        indexes = [
        [0, 0, 1],
        [0, 1, 0],
        [0, 2, 2],
        [1, 2, 2],
        [2, 2, 1],
        [2, 1, 0],
        [2, 0, 3],
        [2, 0, 2]
    ]
        for i in range(len(indexes)): 
            self._make_grid()
            self.grid[indexes[i][0]][indexes[i][1]] = self.loading_cycle[indexes[i][2]]
            print("\n".join(" ".join(row) for row in self.grid))
            time.sleep(0.05)
            #os.system('cls')
        
    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)
    
def main():
    grid = Grid(3, 3)
    try:
        while True:
            grid.load()
    except KeyboardInterrupt:
        while True:
            grid.load()
        
main()
