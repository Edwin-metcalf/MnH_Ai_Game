## by nathaniel hahn for mnh
from power_plant_node import PowerPlantNode

class Stats:
    def __init__(self, version="0.1.0"):
        self.users = 0
        self.energy_used = 0
        self.version = version
        self.energy_produced = 0
        self.money = 0
        #self.connected_nodes = connected_nodes

  
    def update_users(self, score):
        #users based on score 
        self.users = int(score * 10)
    
    def update_money(self, score):
        #money based on score
        self.money = round(score * 2.3, 2)

    
    def update_energy(self, connected_nodes, score_tick):
        self.energy_used += score_tick * 5
        for i in connected_nodes:
            if isinstance(i, PowerPlantNode):
                self.energy_produced += i.energy_produced
            #this will become so inefficient need to process new nodes when they are created/ destroyed 
            # then just update the tick on these update functions instead of looking through  connected nodes each time

            
    



    def get_stats_display(self):
        return [
            f"VERSION: {self.version}",
            f"USERS: {self.users}",
            f"MONEY: ${self.money}",
            f"ENERGY USED: {self.energy_used} kWh",
            f"ENERGY PRODUCED: {self.energy_produced} kWh"
        ]

