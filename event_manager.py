from event import Event

class EventManager:
    def __init__(self):
        pass

    def process_event(self, event):
        print(event.text)
    
    def handle_event_timing(self): #or create an event maybe better wording
        event_gang = Event("oh no you stole everyones data no one likes you")
        #self.process_event(event_gang)

