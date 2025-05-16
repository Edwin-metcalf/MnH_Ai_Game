

class Board:
    #score for now there will be other stats like power vs data use and money but this isplace holder for the vibe stat
    def __init__(self,score):
        width = 40
        height = 10
        self.middle_y = height // 2
        self.middle_x = width // 2
        self.score = score

        self.map_grid = [[" " for _ in range(width)] for _ in range(height)]        
    
    def generate_map(self):
        print( " " + "_" * (len(self.map_grid[0]) - 1))

        for row in self.map_grid:
            print("|" + "".join(row) + "|")

        print( " " + "_" * (len(self.map_grid[0]) - 1))

    def reset_ai_area(self):
        area_size = 5
        for y in range(self.middle_y - area_size, self.middle_y + area_size):
            for x in range(self.middle_x - area_size, self.middle_x + area_size):
                self.map_grid[y][x] = " "
    
    def update_board(self, score):
        self.reset_ai_area()

        if score < 10:
            self.level_1_ai()
        else:
            self.level_2_ai()
        self.generate_map()




    def level_1_ai(self):
        self.map_grid[self.middle_y-1][self.middle_x - 1] = "."
        self.map_grid[self.middle_y-1][self.middle_x] = "-"
        self.map_grid[self.middle_y-1][self.middle_x + 1] = "."

        self.map_grid[self.middle_y][self.middle_x - 1] = "|"
        self.map_grid[self.middle_y][self.middle_x + 1] = "|"

        self.map_grid[self.middle_y+1][self.middle_x - 1] = "'"
        self.map_grid[self.middle_y+1][self.middle_x] = "-"
        self.map_grid[self.middle_y+1][self.middle_x + 1] = "'"

    def level_2_ai(self):
        self.map_grid[self.middle_y-1][self.middle_x - 2] = "."
        self.map_grid[self.middle_y-1][self.middle_x - 1] = "-"
        self.map_grid[self.middle_y-1][self.middle_x] = "-"
        self.map_grid[self.middle_y-1][self.middle_x + 1] = "-"
        self.map_grid[self.middle_y-1][self.middle_x + 2] = "."

        self.map_grid[self.middle_y][self.middle_x - 2] = "|"
        self.map_grid[self.middle_y][self.middle_x + 2] = "|"

        self.map_grid[self.middle_y+1][self.middle_x - 2] = "'"
        self.map_grid[self.middle_y+1][self.middle_x - 1] = "-"
        self.map_grid[self.middle_y+1][self.middle_x] = "-"
        self.map_grid[self.middle_y+1][self.middle_x + 1] = "-"
        self.map_grid[self.middle_y+1][self.middle_x + 2] = "'"

        




