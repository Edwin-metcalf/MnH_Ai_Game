## by nathaniel hahn for mnh
from power_plant_node import PowerPlantNode

class Stats:
    def __init__(self, version="0.1.0"):
        self.users = 0
        self.version = version

        self.energy_produced = 0
        self.energy_used = 0
        self.energy_total = 0

        self.money_total = 0.00
        self.money_produced = 0.00
        self.costs = 0.00
        #self.connected_nodes = connected_nodes

  
    def update_users(self, score):
        #users based on score 
        self.users = int(score * 10)
    
    def update_money(self, score):
        #money based on score
        self.money_produced = round(score * 2.3, 2)
        self.money_total += round(self.money_produced - self.costs, 2)

    
    def update_energy(self, connected_nodes, score_tick):
        self.costs = 0
        if self.energy_total < 0:
            self.energy_total = 0
        self.energy_used += score_tick * 5

        for i in connected_nodes:
            if isinstance(i, PowerPlantNode):
                self.energy_produced += i.energy_produced

        self.energy_total += self.energy_produced - self.energy_used

        if self.energy_total < 0:
            energy_cost = round(abs(self.energy_total) // 7.4, 2)
            self.costs += round(energy_cost, 2)
            print(f"You used {self.energy_total} more then you produced and had to pay ${energy_cost}")

            #this will become so inefficient need to process new nodes when they are created/ destroyed 
            # then just update the tick on these update functions instead of looking through  connected nodes each time

            
    



    def get_stats_display(self):
        return [
            f"VERSION: {self.version}",
            f"USERS: {self.users}",
            f"MONEY: TOTAL ${self.money_total:.2f} MADE: ${self.money_produced:.2f} COSTS: ${self.costs:.2f} ",
            f"ENERGY: USED: {self.energy_used} kWh, PRODUCED: {self.energy_produced} kWh, TOTAL: {self.energy_total} kWh"
        ]

