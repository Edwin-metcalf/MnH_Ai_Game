

class PowerPlantEvent:
    def __init__(self):
        print("you are building a power plant brr brr")
    
    def create_power_plant(self,board,x,y):
        board[y][x+2] = "|"
        board[y][x+3] = "|"

        board[y+1][x+1] = "/"
        board[y+1][x+4] = "\\"
        board[y+1][x+5] = "_"

        board[y+2][x] = "|"
        board[y+2][x+1] = "+"
        board[y+2][x+5] = "+"
        board[y+2][x+6] = "|"
        board[y+2][x+7] = "_"
        board[y+2][x+8] = "_"

        board[y+3][x] = "|"
        board[y+3][x+1] = "_"
        board[y+3][x+2] = "|"
        board[y+3][x+4] = "|"
        board[y+3][x+5] = "_"
        board[y+3][x+6] = "_"
        board[y+3][x+7] = "_"
        board[y+3][x+8] = "_"
        board[y+3][x+9] = "|"
        
        return board




