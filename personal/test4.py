import numpy as np

class Grid:
    
    def __init__(self, grid_height: int = 11, grid_width: int = 11) -> None:
        self.grid_height: int = grid_height
        self.grid_width: int = grid_width
        
        self.empty_cell: str = "#"
        self.filled_cell: str = "@"
        self._make_grid()
        
    def _make_grid(self) -> None :
        self.grid = np.zeros((self.grid_height, self.grid_width), dtype=bool)    
    
    def set_tile(self, y: int = 0, x: int = 1, state: bool = False) -> None:
        if y >= 0 and y < self.grid_height and x >= 0 and x < self.grid_width:
            self.grid[y, x] = state
    
    def __str__(self) -> str:
        return "\n".join(
            " ".join(
                self.filled_cell if item else self.empty_cell for item in row
            )
            for row in self.grid
        )
        
def main() -> None:
    grid = Grid(11, 11)
    grid.set_tile(1, 1, True)
    print(grid)
    
main()