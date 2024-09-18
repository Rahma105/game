# import pygame
# import time
# import random

# pygame.init()

# pygame.mixer.init()
# lobby_sound = pygame.mixer.Sound('image/image/video/audio/audio_2024-09-10_22-18-00.ogg') 
# game_over_sound = pygame.mixer.Sound('image/image/video/audio/spongebob-fail.wav') 
# eat_sound = pygame.mixer.Sound('image/image/video/audio/ukus-zvonkiy.wav') 

# # Цвета
# white = (255, 255, 255)
# yellow = (50, 140, 52)
# black = (24, 100, 250)
# red = (133, 20, 50)
# green = (0, 255, 0)
# blue = (100, 103, 53)

# # Размеры окна
# dis_width = 600
# dis_height = 500
# dis = pygame.display.set_mode((dis_width, dis_height))

# pygame.display.set_caption('Змейка')
# clock = pygame.time.Clock()

# # Размер и скорость змейки
# snake_block = 10
# snake_speed = 15

# # Шрифты
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)

# # Загрузка фонового изображения
# background_image = pygame.image.load('image/image/nike.png')
# background_image = pygame.transform.scale(background_image, (dis_width, dis_height))

# # Функция для отображения счета
# def your_score(score):
#     value = score_font.render("Ваш счёт: " + str(score), True, yellow)
#     dis.blit(value, [0, 0])

# # Функция для отображения змейки
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# # Функция для отображения сообщения
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])

# # Функция для отрисовки кнопки
# def draw_button(text, color, x, y, width, height, action=None):
#     pygame.draw.rect(dis, color, [x, y, width, height])
#     text_surf = font_style.render(text, True, white)
#     text_rect = text_surf.get_rect(center=(x + width / 2, y + height / 2))
#     dis.blit(text_surf, text_rect)
    
#     # Проверка на клик по кнопке
#     mouse_pos = pygame.mouse.get_pos()
#     mouse_click = pygame.mouse.get_pressed()
#     if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
#         if mouse_click[0] == 1 and action:
#             action()

# # Функция для отображения главного меню
# def game_intro():
#     intro = True
#     pygame.mixer.Sound.play(lobby_sound)  # Воспроизведение звука лобби при входе в главное меню
#     while intro:
#         dis.blit(background_image, (0, 0))
#         message("Добро пожаловать в Змейку!", yellow)
#         draw_button("Начать", green, dis_width / 4, dis_height / 2 - 30, 120, 50, game_loop)
#         draw_button("Выход", red, dis_width / 2 + 10, dis_height / 2 - 30, 120, 50, quit_game)
#         pygame.display.update()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

# def quit_game():
#     pygame.quit()
#     quit()

# # Основная игровая функция
# def game_loop():
#     game_over = False
#     game_close = False

#     x1 = dis_width // 2
#     y1 = dis_height // 2

#     x1_change = 0
#     y1_change = 0

#     snake_list = []
#     length_of_snake = 1

#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

#     global snake_speed
#     snake_speed = 15

#     while not game_over:
#         while game_close:
#             pygame.mixer.Sound.play(game_over_sound)

#             dis.blit(background_image, (0, 0))
#             message("Game over! Нажмите C для повторной игры или Q для выхода", red)
#             your_score(length_of_snake - 1)
#             draw_button("Повторить", green, dis_width / 4, dis_height / 2 + 20, 120, 50, game_loop)
#             draw_button("Выход", red, dis_width / 2 + 10, dis_height / 2 + 20, 120, 50, quit_game)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_s:
#                     snake_speed = max(5, snake_speed - 5)
#                 elif event.key == pygame.K_f:
#                     snake_speed += 5

#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True

#         x1 += x1_change
#         y1 += y1_change

#         dis.blit(background_image, (0, 0))
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

#         snake_head = [x1, y1]
#         snake_list.append(snake_head)

#         if len(snake_list) > length_of_snake:
#             del snake_list[0]

#         for x in snake_list[:-1]:
#             if x == snake_head:
#                 game_close = True

#         our_snake(snake_block, snake_list)
#         your_score(length_of_snake - 1)

#         pygame.display.update()

#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             length_of_snake += 1
#             pygame.mixer.Sound.play(eat_sound)

#         clock.tick(snake_speed)

#     pygame.quit()

# game_intro()

import pygame
import random

pygame.init()

pygame.mixer.init()
game_over_sound = pygame.mixer.Sound('image/image/video/audio/spongebob-fail.wav') 
eat_sound = pygame.mixer.Sound('image/image/video/audio/ukus-zvonkiy.wav') 

# Цвета
white = (255, 255, 255)
yellow = (50, 140, 52)
black = (24, 100, 250)
red = (133, 20, 50)
green = (0, 255, 0)

# Размеры окна
dis_width = 600
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

# Размер и скорость змейки
snake_block = 10
snake_speed = 15

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Загрузка фонового изображения
background_image = pygame.image.load('image/image/nike.png')
background_image = pygame.transform.scale(background_image, (dis_width, dis_height))

# Функция для отображения счета
def your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Функция для отображения змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Функция для отображения сообщения
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Функция для отрисовки кнопки
def draw_button(text, color, x, y, width, height, action=None):
    pygame.draw.rect(dis, color, [x, y, width, height])
    text_surf = font_style.render(text, True, white)
    text_rect = text_surf.get_rect(center=(x + width / 2, y + height / 2))
    dis.blit(text_surf, text_rect)
    
    # Проверка на клик по кнопке
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
        if mouse_click[0] == 1 and action:
            action()

# Функция для отображения главного меню
def game_intro():
    intro = True
    while intro:
        dis.blit(background_image, (0, 0))
        message("Добро пожаловать в Змейку!", yellow)
        draw_button("Начать", green, dis_width / 4, dis_height / 2 - 30, 120, 50, game_loop)
        draw_button("Выход", red, dis_width / 2 + 10, dis_height / 2 - 30, 120, 50, quit_game)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def quit_game():
    pygame.quit()
    quit()

# Основная игровая функция
def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    global snake_speed
    snake_speed = 15

    # Добавляем счетчик съеденных фруктов
    fruits_eaten = 0
    big_food = False

    while not game_over:
        while game_close:
            pygame.mixer.Sound.play(game_over_sound)

            dis.blit(background_image, (0, 0))
            message("Game over! Нажмите C для повторной игры или Q для выхода", red)
            your_score(length_of_snake - 1)
            draw_button("Повторить", green, dis_width / 4, dis_height / 2 + 20, 120, 50, game_loop)
            draw_button("Выход", red, dis_width / 2 + 10, dis_height / 2 + 20, 120, 50, quit_game)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.blit(background_image, (0, 0))

        # Если съедено 3 фрукта, создается большой фрукт
        if big_food:
            pygame.draw.rect(dis, red, [foodx, foody, snake_block * 2, snake_block * 2])
        else:
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Проверка на столкновение с едой
        if (x1 == foodx and y1 == foody) or (big_food and x1 in range(int(foodx), int(foodx + snake_block * 2)) and y1 in range(int(foody), int(foody + snake_block * 2))):
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            if big_food:
                length_of_snake *= 2  # Увеличиваем длину змейки в 2 раза
                big_food = False
            else:
                length_of_snake += 1
                fruits_eaten += 1

                # После съеденных 3 фруктов создается большой фрукт
                if fruits_eaten == 3:
                    big_food = True
                    fruits_eaten = 0  # Сбрасываем счетчик

            pygame.mixer.Sound.play(eat_sound)

        clock.tick(snake_speed)

    pygame.quit()

game_intro()
