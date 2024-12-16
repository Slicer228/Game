import pygame
from utils.constants import RED, PLAYER_SIZE, GRAVITY, JUMP_SPEED, PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.vel_y = 0
        self.vel_x = 0
        self.is_jumping = False
        self.spriteR = pygame.transform.scale(pygame.image.load('assets/MarioJumping.png'),(PLAYER_SIZE,PLAYER_SIZE))
        self.spriteL = pygame.transform.scale(pygame.image.load('assets/MarioJumpingA.png'),(PLAYER_SIZE,PLAYER_SIZE))
        self.direction = 'R'
    
    def start_jumping(self):
        self.is_jumping = True
        self.vel_y = JUMP_SPEED
    
    def update(self, screen_width):
        if self.is_jumping:
            
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
            
            
            keys = pygame.key.get_pressed()
            self.vel_x = (keys[pygame.K_d] - keys[pygame.K_a]) * PLAYER_SPEED
            if self.vel_x < 0:
                self.direction = 'L'
            elif self.vel_x > 0:
                self.direction = 'R'
            self.rect.x += self.vel_x
            
            
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > screen_width:
                self.rect.right = screen_width
    
    def handle_platform_collisions(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    if self.rect.bottom > platform.rect.top:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = JUMP_SPEED 
    
    def check_enemy_collisions(self, enemies):
        return any(self.rect.colliderect(enemy.rect) for enemy in enemies)
    
    def draw(self, screen, camera_y):
        if self.direction == 'R':
            screen.blit(self.spriteR, (self.rect.x, self.rect.y - camera_y))
        else:
            screen.blit(self.spriteL, (self.rect.x, self.rect.y - camera_y))
