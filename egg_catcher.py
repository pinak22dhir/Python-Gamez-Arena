import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen_width = screen.get_width()
screen_height = screen.get_height()
pygame.display.set_caption("Egg Catcher Game")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
basket_width = 100
basket_height = 100
basket_x = (screen_width - basket_width) // 2
basket_y = screen_height - basket_height
basket_speed = 10
egg_radius = 20
egg_speed = 3.5
egg_generation_delay = 60
eggs = []
score = 0
lives = 3
eggs_caught = 0
game_over = False
replay = False
control_option = None
paused = False

def draw_basket():
    pygame.draw.rect(screen, WHITE, (basket_x, basket_y, basket_width, basket_height))
    
    
def draw_eggs():
    for egg in eggs:
        pygame.draw.circle(screen, RED, (egg[0], egg[1]), egg_radius)
        
def update_eggs():
    global egg_speed
    for egg in eggs:
        egg[1] += egg_speed
        
def check_collision():
    global score, lives, egg_speed, eggs_caught, game_over
    for egg in eggs:
        if egg[1] + egg_radius > basket_y and egg[0] >= basket_x and egg[0] <= basket_x + basket_width:
            eggs.remove(egg)
            score += 1
            eggs_caught += 1
            if eggs_caught % 5 == 0:
                egg_speed += 0.5
        elif egg[1] + egg_radius > screen_height:
            eggs.remove(egg)
            lives -= 1
            if lives == 0:
                game_over = True
                
def reset_game():
    global score, lives, egg_speed, eggs_caught, game_over, replay, control_option
    score = 0
    lives = 3
    egg_speed = 3.5
    eggs_caught = 0
    game_over = False
    replay = False
    display_control_options()
    eggs.clear()

def toggle_pause():
    global paused
    paused = not paused    
    
def display_control_options():
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    keys_text = font.render("Press K for Keys Control", True, WHITE)
    mouse_text = font.render("Press M for Mouse Control", True, WHITE)
    screen.blit(keys_text, ((screen_width - keys_text.get_width()) // 2, (screen_height - keys_text.get_height()) // 2 - 50))
    screen.blit(mouse_text, ((screen_width - mouse_text.get_width()) // 2, (screen_height - mouse_text.get_height()) // 2 + 50))
    pygame.display.flip()
    
while not control_option:
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    screen.fill((0, 0, 0))
    display_control_options()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                control_option = "keys"
            elif event.key == pygame.K_m:
                control_option = "mouse"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                toggle_pause()

    if paused:
        clock.tick(10)  
        continue        
                
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width = event.w
            screen_height = event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            basket_x = (screen_width - basket_width) // 2
            basket_y = screen_height - basket_height
    if game_over:
        screen.fill((0, 0, 0))
        game_over_text = font.render("Game Over", True, WHITE)
        score_text=font.render("Your score:"+str(score),True,WHITE)
        replay_text = font.render("Press R to replay or Q to quit", True, WHITE)
        screen.blit(game_over_text, ((screen_width - game_over_text.get_width()) // 2, (screen_height - game_over_text.get_height()) // 2))
        screen.blit(score_text, ((screen_width - score_text.get_width()) // 2, (screen_height +20+ score_text.get_height()) // 2))
        screen.blit(replay_text, ((screen_width+20 - replay_text.get_width()) // 2, (screen_height+90+ game_over_text.get_height()) // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    display_control_options()
                elif event.key == pygame.K_q:
                    running = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width = event.w
                screen_height = event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                basket_x = (screen_width - basket_width) // 2
                basket_y = screen_height - basket_height
        screen.fill((0, 0, 0))
        if control_option == "keys":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and basket_x > 0:
                basket_x -= basket_speed
            if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
                basket_x += basket_speed
        elif control_option == "mouse":
            pos = pygame.mouse.get_pos()
            basket_x = pos[0] - basket_width // 2
            if basket_x < 0:
                basket_x = 0
            if basket_x > screen_width - basket_width:
                basket_x = screen_width - basket_width
        if random.randint(0, egg_generation_delay) == 0:
            eggs.append([random.randint(egg_radius, screen_width - egg_radius), 0])
        update_eggs()
        draw_eggs()
        draw_basket()
        check_collision()
        score_text = font.render("Score: " + str(score), True, WHITE)
        lives_text = font.render("Lives: " + str(lives), True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (screen_width - lives_text.get_width() - 10, 10))
        
        
        for egg in eggs:
            if egg[1] + egg_radius > basket_y + basket_height:
                eggs.remove(egg)
        
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
