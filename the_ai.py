from node import Node
from stat_organizer import StatOrganizer

class TheAi:
    def __init__(self, board=None):
        print("Ai created")
        #the main player the ai
        self.power = 0
        self.connected_nodes = []
        self.board = board


    def tick(self):
        power_tick = 0
        for i in self.connected_nodes:
            power_tick += i.bonus
        self.power += power_tick
        print(self.power)



    