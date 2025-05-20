from stats import Stats

class TheAi:
    def __init__(self, board=None, version="0.1.0"):
        print("Ai created")
        #the main player the ai
        self.score = 0
        self.connected_nodes = []
        self.connected_nodes_len = 0
        self.board = board
        self.stats = Stats(version)
        self.current_score_tick = 0


    def tick(self):
        if self.connected_nodes_len != len(self.connected_nodes):
            self.connected_nodes_len = len(self.connected_nodes)
            self.current_score_tick = 0
            for node in self.connected_nodes:
                self.current_score_tick += node.bonus

        self.score += self.current_score_tick
        
        self.update_stats()
        
        if self.board:
            self.board.update_board(self.score, self.stats)
        
        print(f"Score: {self.score}")
        print(f"Current Score Tick: {self.current_score_tick}")
    
    def update_stats(self):
        self.stats.update_users(self.score)
        self.stats.update_energy(self.connected_nodes, self.current_score_tick)



    
