import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
GROUND_HEIGHT = 50
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 30, 30
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner")

# Player
player_x = 50
player_y = HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT
player_speed = 5
jumping = False
max_jump_height = 100  # Define a altura máxima do salto

# Obstacles
obstacles = []

# Clock to control the game loop
clock = pygame.time.Clock()

def draw_player():
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

def draw_ground():
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

def generate_obstacle():
    obstacle_x = WIDTH
    obstacle_y = HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT
    obstacles.append([obstacle_x, obstacle_y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True

    # Update player position
    if jumping and player_y > HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT - max_jump_height:
        player_y -= 10
        if player_y <= HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT - max_jump_height:
            jumping = False
    else:
        player_y += player_speed

    # Ensure player stays within the screen boundaries
    player_y = max(0, min(player_y, HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT))

    # Generate obstacles
    if random.randint(0, 100) < 2:
        generate_obstacle()

    # Update obstacle positions
    for obstacle in obstacles:
        obstacle[0] -= 5

    # Remove obstacles that are out of the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle[0] > -OBSTACLE_WIDTH]

    # Draw everything
    screen.fill(WHITE)
    draw_ground()
    draw_player()
    draw_obstacles()
    pygame.display.flip()

    # Check for collisions
    for obstacle in obstacles:
        if (
            player_x + PLAYER_WIDTH > obstacle[0]
            and player_x < obstacle[0] + OBSTACLE_WIDTH
            and player_y + PLAYER_HEIGHT > obstacle[1]
        ):
            pygame.quit()
            sys.exit()

    clock.tick(60)
 