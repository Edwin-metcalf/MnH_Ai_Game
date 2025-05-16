from the_ai import TheAi
from node import Node
from event_manager import EventManager
from board import Board

class GameManager:
    def __init__(self, version="0.1.0"):
        self.the_map = Board(0)
        self.version = version


    def main_game(self):
        reactor = Node(1)
        event_manager = EventManager()

        the_ai = TheAi(self.the_map, self.version)
        the_ai.connected_nodes.append(reactor)


        choice = input("turn the ai on? ")
        
        while True:
            choice = input("'1' to tick 2 to exit ")
            if the_ai.power >= 10:
                event_manager.handle_event_timing()

            if choice == "1":
                print(the_ai.power)
                the_ai.tick()
            else:
                break
