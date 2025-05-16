## by nathaniel hahn for mnh


class Stats:
    def __init__(self, version="0.1.0"):
        self.users = 0
        self.energy_used = 0
        self.version = version
        #self.energy_produced = 0
  
    def update_users(self, power):
        #users based on power 
        self.users = int(power * 10)
    
    def update_energy(self, connected_nodes, power_tick):
        self.energy_used += power_tick * 5

    def get_stats_display(self):
        return [
            f"VERSION: {self.version}",
            f"USERS: {self.users}",
            f"ENERGY: {self.energy_used} kWh"
        ]

