import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird properties
bird_width, bird_height = 40, 30
bird_x, bird_y = 100, HEIGHT // 2
bird_velocity = 0
gravity = 0.5

# Pipe properties
pipe_width, pipe_gap = 70, 200
pipe_velocity = 4
pipes = []

# Score
score = 0
font = pygame.font.SysFont(None, 50)

def draw_bird():
    pygame.draw.rect(win, WHITE, (bird_x, bird_y, bird_width, bird_height))

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(win, WHITE, pipe)

def display_score():
    score_text = font.render(str(score), True, WHITE)
    win.blit(score_text, (WIDTH // 2 - 20, 50))

def collision_detection():
    if bird_y > HEIGHT or bird_y < 0:
        return True
    for pipe in pipes:
        if pipe.colliderect(pygame.Rect(bird_x, bird_y, bird_width, bird_height)):
            return True
    return False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -10

    bird_velocity += gravity
    bird_y += bird_velocity

    if len(pipes) < 2:
        pipe_x = WIDTH
        pipe_height = random.randint(50, HEIGHT - pipe_gap - 50)
        top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
        bottom_pipe = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_height - pipe_gap)
        pipes.extend([top_pipe, bottom_pipe])

    for pipe in pipes:
        pipe.x -= pipe_velocity
        if pipe.x + pipe_width < 0:
            pipes.remove(pipe)
            score += 1

    if collision_detection():
        running = False

    draw_bird()
    draw_pipes()
    display_score()
    pygame.display.update()

pygame.quit()
