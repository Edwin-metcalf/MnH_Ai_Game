from game_manager import GameManager
from board import Board


def main():
    game = GameManager()
    board = Board(0)
    board.update_score(100)


    while True:
        game.main_game()
        response = input("cancel Y/N? ")
        if response == "y":
            break



if __name__ == "__main__":
    main()