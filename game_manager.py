from the_ai import TheAi
from node import Node
from event_manager import EventManager
from board import Board

class GameManager:
    def __init__(self):
        self.the_map = Board(0)


    def main_game(self):
        reactor = Node(1)
        event_manager = EventManager()

        the_ai = TheAi(self.the_map)
        the_ai.connected_nodes.append(reactor)



        choice = input("turn the ai on? ")
        #self.the_map.level_1_ai()
        
        while True:
            #self.the_map.generate_map()
            choice = input("'1' to tick 2 to exit ")
            if the_ai.power >= 10:
                event_manager.handle_event_timing()
                #self.the_map.reset_ai_area()
                #self.the_map.level_2_ai()
            if choice == "1":
                print(the_ai.power)
                the_ai.tick()
            else:
                break
