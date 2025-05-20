from the_ai import TheAi
from node import Node
from event_manager import EventManager
from board import Board
from power_plant_node import PowerPlantNode

class GameManager:
    def __init__(self, version="0.1.0"):
        self.the_map = Board(0)
        self.version = version


    def main_game(self):
        reactor = Node(1)
        event_manager = EventManager()

        the_ai = TheAi(self.the_map, self.version)
        the_ai.connected_nodes.append(reactor)
        the_map = the_ai.board.map_grid


        choice = input("turn the ai on? ")
        
        while True:
            choice = input("'1' to tick 2 to exit ")
            if the_ai.score == 2:
                the_map = event_manager.power_plant_event(the_map,1,1)

                the_ai.connected_nodes.append(PowerPlantNode(1,525))

            if choice == "1":
                print(the_ai.score)
                the_ai.tick()
            else:
                break
