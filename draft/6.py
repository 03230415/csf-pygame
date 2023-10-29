import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Simple Game')

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create the player character
player = pygame.rect.Rect((screen_width / 2) - 10, (screen_height - 60), 20, 50)

# Create the enemy character
enemy = pygame.rect.Rect(random.randint(0, screen_width - 20), 20, 20, 50)

# Create the game over font
game_over_font = pygame.font.Font(None, 72)

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(black)

    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, enemy)

    # Check for collision
    if player.colliderect(enemy):
        screen.blit(game_over_font.render('Game Over', True, white), (screen_width / 2 - 100, screen_height / 2 - 36))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    # Update player position based on key pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Update enemy position
    enemy.x += random.randint(-5, 5)
    if enemy.x < 0 or enemy.x > screen_width - 20:
        enemy.y += 50

    # Ensure enemy stays on screen
    if enemy.y > screen_height - 20:
        enemy.x = random.randint(0, screen_width - 20)
        enemy.y = 20

    # Ensure player stays on screen
    if player.x < 0:
        player.x = 0
    if player.x > screen_width - 20:
        player.x = screen_width - 20

    # Update the display
    pygame.display.flip()