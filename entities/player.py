import pygame
from utils.constants import RED, PLAYER_SIZE, GRAVITY, JUMP_SPEED, PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.vel_y = 0
        self.vel_x = 0
        self.is_jumping = False
    
    def start_jumping(self):
        self.is_jumping = True
        self.vel_y = JUMP_SPEED
    
    def update(self, screen_width):
        if self.is_jumping:
            # Vertical movement
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
            
            # Horizontal movement
            keys = pygame.key.get_pressed()
            self.vel_x = (keys[pygame.K_d] - keys[pygame.K_a]) * PLAYER_SPEED
            self.rect.x += self.vel_x
            
            # Screen boundaries
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > screen_width:
                self.rect.right = screen_width
    
    def handle_platform_collisions(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:  # Падаем вниз
                    if self.rect.bottom > platform.rect.top:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = JUMP_SPEED  # Автоматический прыжок при касании платформы
    
    def check_enemy_collisions(self, enemies):
        return any(self.rect.colliderect(enemy.rect) for enemy in enemies)
    
    def draw(self, screen, camera_y):
        pygame.draw.rect(screen, RED, 
                        pygame.Rect(self.rect.x, 
                                  self.rect.y - camera_y, 
                                  self.rect.width, 
                                  self.rect.height))