from event import WebScrapeEvent
from power_plant_event import PowerPlantEvent

class EventManager:
    def __init__(self):
        self.web_scrape_event_happened = False
        pass

    def process_event(self, event):
        print(event.text)
    
    def handle_event_timing(self): #or create an event maybe better wording
        #event_gang = Event("oh no you stole everyones data no one likes you")
        #self.process_event(event_gang)
        pass

    def power_plant_event(self,board,x=0,y=0):
        power_plant = PowerPlantEvent()
        new_board = power_plant.create_power_plant(board,x,y)
        return new_board
    
    def web_scrape_event(self):
        self.web_scrape_event_happened = True
        web_scrape_event = WebScrapeEvent()
        answer_dict = web_scrape_event.buy_data_or_scrape()

        cost = answer_dict.get("cost")
        score = answer_dict.get("score")
        
        return [cost, score]
        
        





