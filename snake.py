import pygame
import random
import time

pygame.init()


def check_snake():
    global run, X, Y
    Xx = len(X)
    i = 0
    while i < Xx - 1:
        if snake_x == X[i] and snake_y == Y[i]:
            run = False
        i = i + 1


def draw_menu():
    screen.fill((40, 40, 190))
    screen.blit(TEXT_menu, (230, 100))

    pygame.draw.rect(screen, (240, 200, 200), (posb_new_game[0], posb_new_game[1], 200, 50))
    pygame.draw.rect(screen, (240, 100, 100), (posb_new_game[0], posb_new_game[1], 200, 50), 3)
    screen.blit(text_new_game, (posb_new_game[0] + 40, posb_new_game[1] + 15))

    pygame.draw.rect(screen, (240, 200, 200), (posb_exit[0], posb_exit[1], 200, 50))
    pygame.draw.rect(screen, (240, 100, 100), (posb_exit[0], posb_exit[1], 200, 50), 3)
    screen.blit(text_exit, (posb_exit[0] + 65, posb_exit[1] + 15))

    pygame.draw.rect(screen, (240, 200, 200), (posb_about[0], posb_about[1], 200, 50))
    pygame.draw.rect(screen, (240, 100, 100), (posb_about[0], posb_about[1], 200, 50), 3)
    screen.blit(text_about, (posb_about[0] + 48, posb_about[1] + 15))


def draw_snake():
    Xx = len(X)
    i = 0
    while i < Xx:
        pygame.draw.rect(screen, PINK, (X[i], Y[i], 15, 15,))
        i = i + 1


def eat_food():
    global X, Y, food_x, food_y, snake_x, snake_y, eated
    X.append(snake_x)
    Y.append(snake_y)
    if food_x == snake_x and food_y == snake_y:
        eated = eated + 1
        food_x = random.randrange(30, 570, 15)
        food_y = random.randrange(30, 570, 15)
    else:
        X.pop(0)
        Y.pop(0)


def check_wall():
    global run
    if snake_x < 30:
        run = False
    if snake_x >= 570:
        run = False
    if snake_y < 30:
        run = False
    if snake_y >= 570:
        run = False


def draw_food():
    if food_y > 300:
        color = (233, 161, 78,)
    if food_y <= 300:
        color = (143, 46, 197,)
    pygame.draw.rect(screen, color, (food_x, food_y, 15, 15))


def draw_home():
    i = 0
    x = 0
    y = 0
    while i < 40:
        pygame.draw.rect(screen, YELLOW, (x, 0, 15, 15))
        pygame.draw.rect(screen, BROWN, (x, 0, 15, 15), 1)
        pygame.draw.rect(screen, YELLOW, (x, 15, 15, 15))
        pygame.draw.rect(screen, BROWN, (x, 15, 15, 15), 1)
        pygame.draw.rect(screen, YELLOW, (0, y, 15, 15))
        pygame.draw.rect(screen, BROWN, (0, y, 15, 15), 1)
        pygame.draw.rect(screen, YELLOW, (15, y, 15, 15))
        pygame.draw.rect(screen, BROWN, (15, y, 15, 15), 1)

        pygame.draw.rect(screen, YELLOW, (x, 585, 15, 15))
        pygame.draw.rect(screen, BROWN, (x, 585, 15, 15), 1)
        pygame.draw.rect(screen, YELLOW, (x, 570, 15, 15))
        pygame.draw.rect(screen, BROWN, (x, 570, 15, 15), 1)
        pygame.draw.rect(screen, YELLOW, (585, y, 15, 15))
        pygame.draw.rect(screen, BROWN, (585, y, 15, 15), 1)
        pygame.draw.rect(screen, YELLOW, (570, y, 15, 15))
        pygame.draw.rect(screen, BROWN, (570, y, 15, 15), 1)
        i = i + 1
        x = x + 15
        y = y + 15


def move_snake():
    global snake_x, snake_y, direction, step
    change_to = direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        change_to = "UP"
    if keys[pygame.K_d]:
        change_to = "RIGHT"
    if keys[pygame.K_s]:
        change_to = "DOWN"
    if keys[pygame.K_a]:
        change_to = "LEFT"

    # -----ВЫБОР ДВИЖЕНИЯ:

    if (direction == "LEFT" and change_to != "RIGHT") or (direction == "RIGHT" and change_to != "LEFT") or \
            (direction == "DOWN" and change_to != "UP") or (direction == "UP" and change_to != "DOWN"):
        direction = change_to

    # -----ДВИЖЕНИЕ
    if direction == "UP":
        snake_y = snake_y - step

    if direction == "DOWN":
        snake_y = snake_y + step

    if direction == "RIGHT":
        snake_x = snake_x + step

    if direction == "LEFT":
        snake_x = snake_x - step


def check_buttons():
    global posb_back, posb_exit, posb_about, posb_new_game, run, FLAG_MENU, FLAG_about
    x, y = pygame.mouse.get_pos()
    button = pygame.mouse.get_pressed(3)
    print(button)
    if button[0]:
        if posb_exit[0] < x < posb_exit[0] + 200 and posb_exit[1] < y < posb_exit[1] + 50:
            run = False
        if posb_about[0] < x < posb_about[0] + 200 and posb_about[1] < y < posb_about[1] + 50:
            FLAG_about = True
        if posb_new_game[0] < x< posb_new_game[0] + 200 and posb_new_game[1] < y < posb_new_game[1] +50:
            FLAG_MENU = False

def ABOUT():
    screen.fill(TRUE_YELLOW)
    text1 = FONT.render("THE ЗМЕЯ: НАСЛЕДИE '3310' ", True, (0, 175, 190))
    text2 = FONT.render("Автор: Иван Шмелёв", True, (0, 175, 190))
    text3 = FONT.render("Отдельное спаибо моему учителю Максиму", True, (0, 175, 190))
    text4 = FONT.render("И ТЕБЕ!", True, (0, 175, 200))
    screen.blit(text1, (100, 100))
    screen.blit(text2, (100, 130))
    screen.blit(text3, (100, 160))
    screen.blit(text4, (100, 200))



# Переменные
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка!")
BLACK = (0, 0, 0)
YELLOW = (205, 133, 63)
TRUE_YELLOW = (195, 190, 0)
BROWN = (100, 67, 30,)
WHITE = (255, 255, 255,)
PINK = (254, 189, 205)
MENU1 = (209, 99, 156)
RED = (255, 30, 0)
color = (0, 0, 0,)
food_x = random.randrange(30, 570, 15)
food_y = random.randrange(30, 570, 15)
snake_x = 300
snake_y = 300
direction = "RIGHT"
step = 15
eated = 0
FLAG_MENU = True
FLAG_about = False
X = [snake_x]
Y = [snake_y]
FONT = pygame.font.Font(None, 60)
TEXT_menu = FONT.render("МЕНЮ", True, RED)
FONT = pygame.font.Font(None, 30)
text_new_game = FONT.render("Новая игра", True, (250, 100, 49))
text_exit = FONT.render("Выход", True, (250, 100, 49))
text_about = FONT.render("Об авторе", True, (250, 100, 49))
text_back = FONT.render("Назад", True, (250, 100, 49))

posb_new_game = [200, 200]
posb_exit = [200, 300]
posb_about = [200, 400]
posb_back = [400, 500]

run = True
# Цикл
while run:
    start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if FLAG_MENU == True:
        draw_menu()
        check_buttons()
        if FLAG_about == True:
            ABOUT()

    else:

        # Логика (соблюдайте отступ!)

        move_snake()

        check_wall()

        check_snake()

        eat_food()
        if eated < 5:
            pygame.time.delay(200)
        if eated >= 5:
            if eated < 10:
                pygame.time.delay(150)
        if eated >= 15:
            pygame.time.delay(100)

        # Рисование (соблюдайте отступ!)
        screen.fill(BLACK)
        draw_home()
        draw_food()
        draw_snake()
    pygame.display.update()
    print(time.time() - start)
quit()