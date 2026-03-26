class Grid:
    
    def __init__(self, grid_y, grid_x):
        self.grid_y = grid_y
        self.grid_x = grid_x
        
        self.empty_cell = "#"
        self.grid = []
        
        self._make_grid()
        
    def _make_grid(self):
        for _ in range(self.grid_y):
            self.grid.append([self.empty_cell for _ in range(self.grid_x)])
        
    def __str__(self):
        return "\n".join(" ".join(row) for row in self.grid)
    
    
def main():
    grid = Grid(11, 11)
    print(grid)

if __name__ == "__main__":
    main()
