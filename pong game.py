import pygame
import sys
import math

# In
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 15
CUE_LENGTH = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [0, 0]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Bounce off walls
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocity[0] = -self.velocity[0]
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.velocity[1] = -self.velocity[1]

# Main function
def pool_game():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pool Game")

    balls = pygame.sprite.Group()

    # Create balls
    cue_ball = Ball(WIDTH // 4, HEIGHT // 2, WHITE)
    balls.add(cue_ball)

    for i in range(1, 4):
        balls.add(Ball(WIDTH * (3 / 4) + i * BALL_RADIUS * 2, HEIGHT // 2, RED))

    # Set initial velocities for demo purposes
    cue_ball.velocity = [5, 0]
    for ball in balls.sprites()[1:]:
        ball.velocity = [-5, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update ball positions
        balls.update()

        # Check for collisions with walls
        for ball in balls:
            if ball.rect.left < 0 or ball.rect.right > WIDTH:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.top < 0 or ball.rect.bottom > HEIGHT:
                ball.velocity[1] = -ball.velocity[1]

        # Check for collisions between balls
        pygame.sprite.groupcollide(balls, balls, False, False)

        # Drawing
        screen.fill(BLACK)

        # Draw balls
        for ball in balls:
            pygame.draw.circle(screen, WHITE, ball.rect.center, BALL_RADIUS)

        # Draw cue stick
        pygame.draw.line(screen, WHITE, cue_ball.rect.center, (cue_ball.rect.center[0] + CUE_LENGTH, cue_ball.rect.center[1]), 2)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    pool_game()
