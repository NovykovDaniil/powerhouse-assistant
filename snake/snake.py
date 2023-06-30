import time
import random
import pygame

snake_speed = 15
window_x = 1000
window_y = 600
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Snake")

# Load images
background_image = pygame.image.load("img/background.jpg")
background_image = pygame.transform.scale(background_image, (window_x, window_y))

fruit_width = 30
fruit_height = 30
snake_width = 15
snake_height = 15

available_fruits = [
    pygame.image.load("img/cherry.png"),
    pygame.image.load("img/apple.png"),
    pygame.image.load("img/apples.png"),
]

for i in range(len(available_fruits)):
    available_fruits[i] = pygame.transform.scale(available_fruits[i], (fruit_width, fruit_height))

snake_image = pygame.image.load("img/skills.png")
snake_image = pygame.transform.scale(snake_image, (snake_width, snake_height))

snake_head_image = pygame.image.load("img/head.png")
snake_head_image = pygame.transform.scale(snake_head_image, (snake_width, snake_height))

game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_position = [
    random.randrange(1, (window_x // 10 - 1)) * 10,
    random.randrange(1, (window_y // 10 - 1)) * 10,
]
fruit_spawn = True

direction = "RIGHT"
change_to = direction

score = 0

# Set initial fruit image
current_fruit_index = 0
fruit_image = available_fruits[current_fruit_index]


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont("arial", 50)
    game_over_surface = my_font.render("Your Score is: " + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    if (
            snake_position[0] >= fruit_position[0] - snake_width
            and snake_position[0] <= fruit_position[0] + fruit_width
            and snake_position[1] >= fruit_position[1] - snake_height
            and snake_position[1] <= fruit_position[1] + fruit_height
    ):
        score += 10
        fruit_spawn = False
        current_fruit_index = (current_fruit_index + 1) % len(available_fruits)
        fruit_image = available_fruits[current_fruit_index]
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (window_x // 10 - 1)) * 10,
            random.randrange(1, (window_y // 10 - 1)) * 10,
        ]
        fruit_spawn = True

    game_window.blit(background_image, (0, 0))

    for pos in snake_body:
        if pos == snake_body[0]:
            game_window.blit(snake_head_image, (pos[0], pos[1]))
        else:
            game_window.blit(snake_image, (pos[0], pos[1]))

    game_window.blit(fruit_image, (fruit_position[0], fruit_position[1]))

    if snake_position[0] < 0 or snake_position[0] > window_x - snake_width:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - snake_height:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, "arial", 20)
    pygame.display.update()
    fps.tick(snake_speed)
