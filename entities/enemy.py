import pygame
import math
from utils.constants import BLUE, ENEMY_SIZE

class Enemy:
    def __init__(self, x, y, movement_type):
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.movement_type = movement_type
        self.time = 0
        self.start_x = x
        self.start_y = y
        self.amplitude = {
            "horizontal": 100,
            "vertical": 50,
            "circular": 50
        }
    
    def update(self):
        self.time += 0.05
        if self.movement_type == "horizontal":
            self.rect.x = self.start_x + math.sin(self.time) * self.amplitude["horizontal"]
        elif self.movement_type == "vertical":
            self.rect.y = self.start_y + math.sin(self.time) * self.amplitude["vertical"]
        elif self.movement_type == "circular":
            self.rect.x = self.start_x + math.cos(self.time) * self.amplitude["circular"]
            self.rect.y = self.start_y + math.sin(self.time) * self.amplitude["circular"]
    
    def draw(self, screen, camera_y):
        pygame.draw.rect(screen, BLUE, 
                        pygame.Rect(self.rect.x, 
                                  self.rect.y - camera_y, 
                                  self.rect.width, 
                                  self.rect.height))