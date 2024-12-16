class GameState:
    def __init__(self):
        self.is_playing = False
        self.game_over_v = False
    
    def start_game(self):
        self.is_playing = True
        self.game_over_v = False
    
    def game_over(self):
        self.is_playing = False
        self.game_over_v = True