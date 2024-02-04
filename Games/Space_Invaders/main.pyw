import math
import random
import pygame
from pygame import mixer

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load background image
background = pygame.image.load('.\\Games\\Space_Invaders\\background.png')

# Background music
mixer.music.load(".\\Games\\Space_Invaders\\background.wav")
mixer.music.play(-1)

# Set caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('.\\Games\\Space_Invaders\\ufo.png')
pygame.display.set_icon(icon)

# Load player image and set initial position
playerImg = pygame.image.load('.\\Games\\Space_Invaders\\player.png')
player_width = playerImg.get_width()
player_height = playerImg.get_height()
playerX = screen_width / 2 - player_width / 2
playerY = screen_height - player_height - 10
playerX_change = 0

# Load enemy image and set initial position
enemyImg = pygame.image.load('.\\Games\\Space_Invaders\\enemy.png')
enemy_width = enemyImg.get_width()
enemy_height = enemyImg.get_height()
num_of_enemies = 6
enemies = []

for i in range(num_of_enemies):
    enemyX = random.randint(0, screen_width - enemy_width)
    enemyY = random.randint(50, 150)
    enemyX_change = random.choice([-1, 1])
    enemyY_change = 40
    enemies.append([enemyX, enemyY, enemyX_change, enemyY_change])

# Load bullet image and set initial position
bulletImg = pygame.image.load('.\\Games\\Space_Invaders\\bullet.png')
bullet_width = bulletImg.get_width()
bullet_height = bulletImg.get_height()
bulletX = 0
bulletY = playerY
bulletY_change = 5
bullet_state = "ready"

# Set initial score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Set game over font
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Function to display score
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Function to display game over message
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Function to draw player
def player(x, y):
    screen.blit(playerImg, (x, y))

# Function to draw enemy
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Function to draw bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + player_width / 2 - bullet_width / 2, y - bullet_height))

# Function to check collision
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    return False

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound(".\\Games\\Space_Invaders\\laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= screen_width - player_width:
        playerX = screen_width - player_width

    for enemy in enemies:
        enemy[0] += enemy[2]
        if enemy[0] <= 0:
            enemy[2] = 1
            enemy[1] += enemy[3]
        elif enemy[0] >= screen_width - enemy_width:
            enemy[2] = -1
            enemy[1] += enemy[3]

        collision = isCollision(enemy[0], enemy[1], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound(".\\Games\\Space_Invaders\\explosion.wav")
            explosion_sound.play()
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            enemy[0] = random.randint(0, screen_width - enemy_width)
            enemy[1] = random.randint(50, 150)

        enemy(enemy[0], enemy[1])

    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(10, 10)

    pygame.display.update()

pygame.quit()
