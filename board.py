

class Board:
    #score for now there will be other stats like power vs data use and money but this isplace holder for the vibe stat
    def __init__(self,score):
        width = 40
        height = 10
        self.middle_y = height // 2
        self.middle_x = width // 2
        self.score = score
        self.stats_display = []

        self.map_grid = [[" " for _ in range(width)] for _ in range(height)]        
    
    def generate_map(self):
        if self.stats_display:
            for stat_line in self.stats_display:
                print(stat_line)
            print("")
        print( " " + "_" * (len(self.map_grid[0]) - 1))

        for row in self.map_grid:
            print("|" + "".join(row) + "|")

        print( " " + "_" * (len(self.map_grid[0]) - 1))

    def reset_ai_area(self):
        area_size = 5
        for y in range(self.middle_y - area_size, self.middle_y + area_size):
            for x in range(self.middle_x - area_size, self.middle_x + area_size):
                self.map_grid[y][x] = " "
    
    def update_board(self, score, stats=None):
        self.reset_ai_area()
        if stats:
            self.stats_display = stats.get_stats_display()

        if score < 10:
            self.level_1_ai()
        else:
            self.level_2_ai()
        self.update_score(score)
        self.generate_map()

    def update_score(self, score):
        list_score = [digit for digit in str(score)]
        print(list_score)
        print(self.middle_x)
        print(self.middle_y)
        if len(list_score) == 1:
            print(f"poopy wanted a name: {len(self.map_grid)} {len(self.map_grid[0])}")
            self.map_grid[self.middle_y][self.middle_x] = list_score[0]
        elif len(list_score) == 2:
            self.map_grid[self.middle_y][self.middle_x] = list_score[1]
            self.map_grid[self.middle_y][self.middle_x - 1] = list_score[0]
        


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
        self.map_grid[self.middle_y-1][self.middle_x + 1] = "."

        self.map_grid[self.middle_y][self.middle_x - 2] = "|"
        self.map_grid[self.middle_y][self.middle_x + 1] = "|"

        self.map_grid[self.middle_y+1][self.middle_x - 2] = "'"
        self.map_grid[self.middle_y+1][self.middle_x - 1] = "-"
        self.map_grid[self.middle_y+1][self.middle_x] = "-"
        self.map_grid[self.middle_y+1][self.middle_x + 1] = "'"

        




