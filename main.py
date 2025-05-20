from game_manager import GameManager



def main():
    game = GameManager()


    while True:
        game.main_game()
        response = input("cancel Y/N? ")
        if response == "y":
            break



if __name__ == "__main__":
    main()