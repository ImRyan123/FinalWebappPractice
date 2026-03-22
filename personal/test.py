import os, time

def clear():
    os.system("cls")

class Grid:
    
    def __init__(self, grid_y, grid_x):
        self.grid_y = grid_y
        self.grid_x = grid_x
        
        self.player_position = [self.grid_y // 2, self.grid_x // 2]
        
        self.empty_cell = "#"
        self.player_cell = "@"
        self.grid = []
        
        self._make_grid()
        
    def _make_grid(self):
        for _ in range(self.grid_y):
            self.grid.append([self.empty_cell for x in range(self.grid_x)])
        
    def move_player(self, index):
        new_y = index[0] + self.player_position[0]
        new_x = index[1] + self.player_position[1]
        
        if new_y >= 0 and new_y < self.grid_y and new_x >= 0 and new_x < self.grid_x:
            new_y, new_x = self.player_position
        else:
            print("ERROR")
        
    def __str__(self):
        rows = []

        for y, row in enumerate(self.grid):
            if y == self.player_position[0]:
                new_row = []
                for x in range(len(row)):
                    if x == self.player_position[1]:
                        new_row.append(self.player_cell)
                    else:
                        new_row.append(self.empty_cell)
                rows.append("  ".join(new_row))
            else:
                rows.append("  ".join(row))

        return "\n".join(rows)

def main(delay):
    grid = Grid(11, 11)    
    while True:
        print(grid)
        time.sleep(delay)
        grid.move_player((-1, 0))
        clear()
        
    
main(0.05)
