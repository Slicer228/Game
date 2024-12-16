class Camera:
    def __init__(self, screen_height):
        self.y = 0
        self.screen_height = screen_height
    
    def update(self, player):
        # Camera follows player only when they go above middle of screen
        if player.rect.top < self.y + self.screen_height // 2:
            self.y = player.rect.top - self.screen_height // 2