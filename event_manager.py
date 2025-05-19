from event import Event
from power_plant_event import PowerPlantEvent

class EventManager:
    def __init__(self):
        pass

    def process_event(self, event):
        print(event.text)
    
    def handle_event_timing(self): #or create an event maybe better wording
        event_gang = Event("oh no you stole everyones data no one likes you")
        #self.process_event(event_gang)

    def power_plant_event(self,board,x=0,y=0):
        power_plant = PowerPlantEvent()
        new_board = power_plant.create_power_plant(board,x,y)
        return new_board


