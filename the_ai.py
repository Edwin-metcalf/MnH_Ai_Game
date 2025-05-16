from node import Node
from stat_organizer import StatOrganizer
from stats import Stats

class TheAi:
    def __init__(self, board=None, version="0.1.0"):
        print("Ai created")
        #the main player the ai
        self.power = 0
        self.connected_nodes = []
        self.board = board
        self.stats = Stats(version)
        self.current_power_tick = 0


    def tick(self):
        power_tick = 0
        for node in self.connected_nodes:
            power_tick += node.bonus
        
        self.current_power_tick = power_tick
        self.power += power_tick
        
        self.update_stats()
        
        if self.board:
            self.board.update_board(self.power, self.stats)
        
        print(f"Power: {self.power}")
    
    def update_stats(self):
        self.stats.update_users(self.power)
        self.stats.update_energy(self.connected_nodes, self.current_power_tick)


    
