import pygame
import random
import sys
from os import listdir

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")


# Определение класса змейки
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * GRID_SIZE)), (cur[1] + (y * GRID_SIZE)))
        if (
            new in self.positions[2:]
            or not (0 <= new[0] < SCREEN_WIDTH)
            or not (0 <= new[1] < SCREEN_HEIGHT)
        ):
            self.reset()
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return True

    def reset(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


# Определение класса еды
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)


# Определение констант направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Определение размеров сетки
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

# Создание змейки и еды
snake = Snake()
food = Food()

# Определение таймера
clock = pygame.time.Clock()

# Основной игровой цикл
while True:
    # Обработка нажатий клавиш
    snake.handle_keys()

    # Перемещение змейки
    snake.move()

    # Проверка на столкновение с едой
    if snake.get_head_position() == food.position:
        snake.length += 1
        food.randomize_position()

    # Отрисовка экрана
    screen.fill(WHITE)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.update()

    # Ограничение частоты кадров
    clock.tick(10)
