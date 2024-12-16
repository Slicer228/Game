import pygame
from utils.constants import GREEN, PLATFORM_WIDTH, PLATFORM_HEIGHT

class Platform:
    def __init__(self, x, y, width=PLATFORM_WIDTH):
        self.rect = pygame.Rect(x, y, width, PLATFORM_HEIGHT)
    
    def draw(self, screen, camera_y):
        pygame.draw.rect(screen, GREEN, 
                        pygame.Rect(self.rect.x, 
                                  self.rect.y - camera_y, 
                                  self.rect.width, 
                                  self.rect.height))