import pygame
pygame.init()
import sys
from utils.constants import BLACK, WHITE, screen, WIDTH, HEIGHT
from entities.player import Player
from game_state import GameState
from camera import Camera
from generators.level_generator import LevelGenerator
from score import ScoreManager

def main():
    
    clock = pygame.time.Clock()
    game_state = GameState()
    camera = Camera(HEIGHT)
    level_generator = LevelGenerator(WIDTH, HEIGHT)
    score_manager = ScoreManager()
    
    def reset_game():
        nonlocal player, platforms, enemies, camera
        player = Player(WIDTH // 2, HEIGHT - 100)
        camera = Camera(HEIGHT)
        platforms = level_generator.generate_initial_platforms()
        enemies = []
        score_manager.score = 0
        score_manager.highest_y = 0
    
    # Initialize game objects
    player = None
    platforms = []
    enemies = []
    reset_game()
    player_pos_b = 1
    font = pygame.font.Font(None, 74)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_state.is_playing:
                        game_state.start_game()
                        reset_game()
                        player.start_jumping()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        if game_state.is_playing:
            # Update
            player.update(WIDTH)
            camera.update(player)
            
            # Generate new platforms and enemies
            if player.rect.top < HEIGHT * player_pos_b:
                player_pos_b -= 1
                new_platforms, new_enemies = level_generator.generate_new_section(camera.y)
                platforms.extend(new_platforms)
                enemies.extend(new_enemies)
            
            # Update enemies
            for enemy in enemies:
                enemy.update()
            
            # Check collisions
            player.handle_platform_collisions(platforms)
            
            if player.check_enemy_collisions(enemies) or player.rect.top > camera.y + HEIGHT:
                game_state.game_over()
            
            # Clean up off-screen objects
            platforms = [p for p in platforms if p.rect.y < (camera.y + HEIGHT)]
            enemies = [e for e in enemies if e.rect.y < (camera.y + HEIGHT)]
            
            # Update score
            score_manager.update_score(-player.rect.top)
        
        # Draw
        screen.fill(BLACK)
        
        if game_state.is_playing:
            # Draw game objects
            for platform in platforms:
                platform.draw(screen, camera.y)
            for enemy in enemies:
                enemy.draw(screen, camera.y)
            player.draw(screen, camera.y)
            
            # Draw score
            score_text = font.render(f"Score: {score_manager.score}", True, WHITE)
            screen.blit(score_text, (10, 10))
        else:
            # Draw start/game over screen
            if game_state.game_over_v:
                text = font.render(f"Game Over! Score: {score_manager.score}", True, WHITE)
                instruction_text = font.render("Press SPACE to Restart", True, WHITE)
            else:
                text = font.render("Press SPACE to Start", True, WHITE)
                instruction_text = font.render("Use A/D to move", True, WHITE)
            
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            instruction_rect = instruction_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 80))
            screen.blit(text, text_rect)
            screen.blit(instruction_text, instruction_rect)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()