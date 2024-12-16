import random
from utils.constants import (
    PLATFORM_WIDTH, ENEMY_SIZE, PLATFORM_MIN_SPACING,
    PLATFORM_MAX_SPACING, ENEMY_SPAWN_CHANCE, PLATFORM_HEIGHT
)
from entities.platform import Platform
from entities.enemy import Enemy

class LevelGenerator:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.last_platform_y = self.screen_height - PLATFORM_HEIGHT
        self.highest_platform_y = self.last_platform_y
    
    def generate_initial_platforms(self):
        platforms = []
        
        platforms.append(Platform(0, self.screen_height - PLATFORM_HEIGHT, self.screen_width))
        
        
        current_y = self.screen_height - 200
        while current_y > -self.screen_height:
            x = random.randint(0, self.screen_width - int(PLATFORM_WIDTH))
            platforms.append(Platform(x, current_y))
            current_y -= random.randint(PLATFORM_MIN_SPACING, PLATFORM_MAX_SPACING)
        
        self.highest_platform_y = current_y
        return platforms
    
    def generate_new_section(self, camera_y):
        platforms = []
        enemies = []
        
        
        current_y = self.highest_platform_y
        
        
        while current_y > camera_y - self.screen_height:
            x = random.randint(0, self.screen_width - int(PLATFORM_WIDTH))
            spacing = random.randint(PLATFORM_MIN_SPACING, PLATFORM_MAX_SPACING)
            current_y -= spacing
            
            
            platforms.append(Platform(x, current_y))
            
            
            if random.random() < ENEMY_SPAWN_CHANCE:
                enemy_x = random.randint(0, self.screen_width - int(ENEMY_SIZE))
                enemy_y = current_y - ENEMY_SIZE - 20
                movement_type = random.choice(["horizontal", "vertical", "circular"])
                enemies.append(Enemy(enemy_x, enemy_y, movement_type))
        
        self.highest_platform_y = current_y  
        return platforms, enemies