import pygame
import time
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
FPS = 15

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (SNAKE_SIZE, 0)

# Initial food position
food = (WIDTH // 2, HEIGHT // 2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, SNAKE_SIZE):
                snake_direction = (0, -SNAKE_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -SNAKE_SIZE):
                snake_direction = (0, SNAKE_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (SNAKE_SIZE, 0):
                snake_direction = (-SNAKE_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-SNAKE_SIZE, 0):
                snake_direction = (SNAKE_SIZE, 0)

    # Move the snake
    snake.insert(0, (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1]))

    # Check for collisions with walls or itself
    if (
        snake[0][0] < 0
        or snake[0][0] >= WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= HEIGHT
        or snake[0] in snake[1:]
    ):
        running = False

    # Check if snake ate the food
    if snake[0] == food:
        food = (random.randrange(0, WIDTH, SNAKE_SIZE), random.randrange(0, HEIGHT, SNAKE_SIZE))
    else:
        snake.pop()

    # Draw everything
    window.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(window, RED, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
