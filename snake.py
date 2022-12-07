import pygame
import random

pygame.init()

def check_snake():
    global run, X, Y
    Xx = len(X)
    i = 0
    while  i < Xx - 1:
        if snake_x == X[i] and snake_y == Y[i]:
            run = False
        i = i + 1

def draw_MENU():
    screen.fill(MENU1)
    # screen.blit()



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


# Переменные
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка!")
BLACK = (0, 0, 0)
YELLOW = (205, 133, 63)
BROWN = (100, 67, 30,)
WHITE = (255, 255, 255,)
PINK = (254, 189, 205)
MENU1 = (209, 99, 156 )
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
X = [snake_x]
Y = [snake_y]
FONT = pygame.font.Font(None,60)
TEXT_menu = FONT.render("меню",True, RED)

run = True
# Цикл
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if FLAG_MENU == True:
        draw_MENU()
    else:

        # Логика (соблюдайте отступ!)

        def draw_menu():
            screen.fill((40, 40, 190))
            screen.blit(TEXT_menu, (230, 100))

        move_snake()

        check_wall()

        check_snake()

        eat_food()
        if eated < 2:
            pygame.time.delay(150)
        if eated >= 2:
            if eated < 4:
                pygame.time.delay(100)
        if eated >= 4:
            pygame.time.delay(50)

        # Рисование (соблюдайте отступ!)
        screen.fill(BLACK)
        draw_home()
        draw_food()
        draw_snake()
    pygame.display.update()
quit()
