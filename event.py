

class Event:
    def __init__(self, text):
        self.text = text
        print(f"{self.text} is happening")

class WebScrapeEvent:
    def __init__(self):
        pass

    def buy_data_or_scrape(self):
        print("You AI needs more data to be trained do you buy data or scrape it?")
        output = {}
        while True:
            response = input("1 to buy data 2 to scrape: ")
            if response == "1":
                print("You bought data it cost $300, it will definitly improve the AI")
                output["cost"] = -300
                output["score"] = 5
                #output["public eye"] = x
                #when we add stat like public perspective this would effect it 


            elif response == "2":
                print("You chose to scrape off lots of major sites, the legality and morality is in a grey area but your AI will improve")
                output["cost"] = 0
                output["score"] = 5
                


            else: 
                print("that is an invalid input please try '1' or '2' ")
            
            return output
            



        
    