from node import Node

class PowerPlantNode(Node):
    def __init__(self, bonus, energy_produced):
        super().__init__(bonus)
        self.bonus = bonus + 3
        self.energy_produced = energy_produced


