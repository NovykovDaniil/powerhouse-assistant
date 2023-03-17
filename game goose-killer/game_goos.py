import pygame
import random
from os import listdir
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, USEREVENT

pygame.init()
FPS = pygame.time.Clock()
screen = width, heigth = 1300, 800
main_surface = pygame.display.set_mode(screen)

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)

BG_PATH = 'image/background'

BG_images = [pygame.image.load(BG_PATH + '/' + file).convert() for file in listdir(BG_PATH)]
bg = pygame.transform.scale(BG_images[0], screen)

enemies = []
bonuses = []
IMGS_PATH = 'image\goose'

Goose_images = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in listdir(IMGS_PATH)]
Goose = Goose_images[0]
N = 3
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3
game_bonuses = 0
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0


def exit(point):
    print(point)
    return False


def creat_enemy():
    enemy = pygame.image.load('image\enemy.png').convert_alpha()
    e = (enemy.get_size())
    enemy_rect = pygame.Rect(width, random.randint(e[1], heigth - e[1]), *enemy.get_size())
    enemy_speed = random.randint(1, 7)
    return [enemy, enemy_rect, enemy_speed]


def creat_bonus():
    bonus = pygame.image.load('image/bonus.png').convert_alpha()
    b = (bonus.get_size())
    bonus_rect = pygame.Rect(random.randint(b[0], width - b[0]), 0, *bonus.get_size())
    bonus_speed = random.randint(1, 5)
    return [bonus, bonus_rect, bonus_speed]


Goose_rect = Goose.get_rect()
Goose_speed = 6
image_index = 0
is_working = True

while is_working:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = exit(game_bonuses)
        if event.type == CREATE_ENEMY:
            enemies.append(creat_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(creat_bonus())
        if event.type == CHANGE_IMG:
            image_index += 1

    Pressed_key = pygame.key.get_pressed()
    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()
    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))

    if N <= game_bonuses < 3 * N:
        bg = pygame.transform.scale(BG_images[1], screen)
    if 3 * N <= game_bonuses:
        bg = pygame.transform.scale(BG_images[2], screen)

        bg_speed = 0
        bgX = 0
        bgX2 = bg.get_width()

    if image_index == len(Goose_images):
        image_index = 0

    Goose = Goose_images[image_index]
    main_surface.blit(Goose, Goose_rect)

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if Goose_rect.colliderect(enemy[1]):
            is_working = exit(game_bonuses)
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])
        if Goose_rect.colliderect(bonus[1]):
            game_bonuses += 1
            bonuses.pop(bonuses.index(bonus))
        else:
            if bonus[1].bottom > heigth:
                bonuses.pop(bonuses.index(bonus))

    # print result
    my_font = pygame.font.Font('font/UA Propisi.ttf', 35)
    main_surface.blit(my_font.render('Бонуси ' + str(game_bonuses), 1, (255, 180, 255)), (width - 130, 30))

    if Pressed_key[K_DOWN] and Goose_rect.bottom < heigth:
        Goose_rect = Goose_rect.move(0, Goose_speed)
    if Pressed_key[K_UP] and Goose_rect.top > 0:
        Goose_rect = Goose_rect.move(0, -Goose_speed)
    if Pressed_key[K_LEFT] and Goose_rect.left > 0:
        Goose_rect = Goose_rect.move(-Goose_speed, 0)
    if Pressed_key[K_RIGHT] and Goose_rect.right < width:
        Goose_rect = Goose_rect.move(Goose_speed, 0)
    main_surface.blit(Goose, Goose_rect)
    pygame.display.flip()

pygame.display.quit()
pygame.quit()


