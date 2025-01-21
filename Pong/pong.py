import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# Clock to control frame rate
clock = pygame.time.Clock()

# Paddle class
class Paddle:
    def __init__(self, x, y, width=10, height=100, speed=7):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self, x, y, radius=7, speed_x=5, speed_y=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Collision with top and bottom
        if self.y - self.radius <= 0 or self.y + self.radius >= WINDOW_HEIGHT:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.x, self.y), self.radius)

    def reset(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.speed_x *= -1
        self.speed_y = 5 * (-1 if self.speed_y > 0 else 1)

# Paddles
left_paddle = Paddle(20, WINDOW_HEIGHT//2 - 50)
right_paddle = Paddle(WINDOW_WIDTH - 30, WINDOW_HEIGHT//2 - 50)

# Ball
ball = Ball(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# Scores
left_score = 0
right_score = 0

# Font for displaying scores
font = pygame.font.SysFont(None, 36)

def handle_input():
    keys = pygame.key.get_pressed()

    # Left paddle controls (W and S)
    if keys[pygame.K_w]:
        left_paddle.move_up()
    if keys[pygame.K_s]:
        left_paddle.move_down()

    # Right paddle controls (Up and Down arrows)
    if keys[pygame.K_UP]:
        right_paddle.move_up()
    if keys[pygame.K_DOWN]:
        right_paddle.move_down()

def check_collision():
    global left_score, right_score
    ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius*2, ball.radius*2)

    if ball_rect.colliderect(left_paddle.rect):
        ball.speed_x *= -1
        ball.x = left_paddle.rect.right + ball.radius
        # hit_sound.play()  # Uncomment if sound is added

    if ball_rect.colliderect(right_paddle.rect):
        ball.speed_x *= -1
        ball.x = right_paddle.rect.left - ball.radius
        # hit_sound.play()  # Uncomment if sound is added

def draw_scores():
    score_text = font.render(f"{left_score}     {right_score}", True, WHITE)
    window.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, 20))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    handle_input()
    ball.move()
    check_collision()

    # Check for scoring
    if ball.x < 0:
        right_score += 1
        # score_sound.play()  # Uncomment if sound is added
        ball.reset()
    elif ball.x > WINDOW_WIDTH:
        left_score += 1
        # score_sound.play()  # Uncomment if sound is added
        ball.reset()

    # Drawing
    window.fill(BLACK)
    left_paddle.draw(window)
    right_paddle.draw(window)
    ball.draw(window)
    draw_scores()

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)