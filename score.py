class ScoreManager:
    def __init__(self):
        self.score = 0
        self.highest_y = 0
    
    def update_score(self, current_y):
        if current_y > self.highest_y:
            self.score = int(current_y)
            self.highest_y = current_y