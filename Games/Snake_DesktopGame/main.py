# SNAKE GAME level1
import pygame as p
import random as r
p.mixer.init()
p.init()
# color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (1, 236, 5)
blue = (0, 245, 214)
yellow = (255, 211, 0)
brown=(138,54,15)
# creating game window
game_window = p.display.set_mode((400, 400))
#background
bgimg = p.image.load("outro.jpg")
bg = p.image.load("intro.jpg")
b = p.image.load("gw.jpg")
w = p.image.load("won.jpg")
bgimg = p.transform.scale(bgimg, (400, 400)).convert_alpha()
bg = p.transform.scale(bg, (400, 400)).convert_alpha()
b = p.transform.scale(b, (400, 400)).convert_alpha()
w = p.transform.scale(w, (400, 400)).convert_alpha()
# GAME TITLE
p.display.set_caption("SNAKE")

p.display.update()
clock = p.time.Clock()   # this is use for time

# creating function for score
font = p.font.SysFont(None, 45)
def score_screen(text, color, x, y):
    screen_score = font.render(text, True, color)
    game_window.blit(screen_score, [x, y])
# creating function for snake length
def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        p.draw.rect(game_window, color, [x, y, snake_size, snake_size])
# creating welcome
font = p.font.SysFont(None, 70)
def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(blue)
        game_window.blit(bg, (0, 0))

        for event in p.event.get():
            if event.type == p.QUIT:  # controlling events
                exit_game = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    gameloop()

        p.display.update()
        clock.tick(40)

# creating a game loop
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    won_game=False
    snake_x = 68
    snake_y = 145
    velocity_x = 0
    m_velocity = 2
    velocity_y = 0
    snake_size = 10
    apple_x = r.randint(0, 400)
    apple_y = r.randint(0, 400)
    score = 0
    fps = 40
    snake_list = []
    snake_length = 1

    while not exit_game:
        # game won window
        if won_game:
            game_window.fill(blue)
            game_window.blit(w,(0, 0))

            for event in p.event.get():
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        exit_game = True
        else:
            if game_over:
                game_window.fill(blue)
                game_window.blit(bgimg, (0, 0))

                for event in p.event.get():
                    if event.type == p.QUIT:  # controlling events
                        exit_game = True
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_ESCAPE:
                            exit_game = True
                        if event.key == p.K_RETURN:
                            welcome()
            else:
                for event in p.event.get():
                    if event.type == p.QUIT:  # controlling events
                        exit_game = True
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_RIGHT:
                            velocity_x = m_velocity
                            velocity_y = 0

                        if event.key == p.K_LEFT:
                            velocity_x = -m_velocity
                            velocity_y = 0

                        if event.key == p.K_UP:
                            velocity_y = -m_velocity
                            velocity_x = 0

                        if event.key == p.K_DOWN:
                            velocity_y = m_velocity
                            velocity_x = 0

                snake_x += velocity_x   # it will give velocity to our snake in x direction
                snake_y += velocity_y   # it will give velocity to our snake in y direction

                if score > 10:
                    m_velocity = 3
                if score > 25:
                    m_velocity = 5
                if score > 40:
                    m_velocity = 7

                if abs(snake_x - apple_x) < 6 and abs(snake_y - apple_y) < 6:
                    score += 2
                    apple_x = r.randint(0,350)   # position of apple
                    apple_y = r.randint(0, 350)
                    snake_length += 3    # increase length of snake
                    p.mixer.music.load("eat.mp3")
                    p.mixer.music.play()
                 # controlling game window
                game_window.fill(yellow)
                game_window.blit(b, (0, 0))
                score_screen("score = "+str(score), green, 100, 5)
                p.draw.rect(game_window, red, [apple_x, apple_y, snake_size, snake_size])
                # through this we can see one head in screen
                head = []
                head.append(snake_x)
                head.append(snake_y)
                snake_list.append(head)
                # this will cut one head as it posses
                if len(snake_list) > snake_length:
                    del snake_list[0]
                # snake overlapping make game over
                if head in snake_list[:-1]:
                    game_over = True
                    p.mixer.music.load("bomb.mp3")
                    p.mixer.music.play()
                # game over
                if snake_x < 0 or snake_x > 400 or snake_y < 0 or snake_y > 400:
                    game_over = True
                    p.mixer.music.load("bomb.mp3")
                    p.mixer.music.play()
                # game won
                if score == 50:
                    won_game = True
                    p.mixer.music.load("won.mp3")
                    p.mixer.music.play()
            plot_snake(game_window, black,snake_list, snake_size)
        p.display.update()
        clock.tick(fps)
    p.quit()
    quit()
welcome()



