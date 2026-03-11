import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Задаем цвета в формате RGB
GRAY = (180, 180, 180)
DARK_GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_body(surface, x, y, width, height, color):
    '''
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра тела
    width, height - ширина и высота тела
    color - цвет
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_head(surface, x, y, size, color):
    '''
    Рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра головы
    size - диаметр головы
    color - цвет
    '''
    circle(surface, color, (x, y), size // 2)

def draw_ear(surface, x, y, width, height, color, outline_color):
    '''
    Рисует ухо зайца с контуром.
    surface - объект pygame.Surface
    x, y - координаты центра уха
    width, height - ширина и высота уха
    color - основной цвет
    outline_color - цвет контура
    '''
    # Основная часть уха
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    # Контур уха
    ellipse(surface, outline_color, (x - width // 2, y - height // 2, width, height), 2)

def draw_eye(surface, x, y, size):
    '''
    Рисует глаз зайца (белок, зрачок, блик).
    surface - объект pygame.Surface
    x, y - координаты центра глаза
    size - размер глаза
    '''
    # Белок глаза
    circle(surface, WHITE, (x, y), size // 2)
    # Зрачок
    circle(surface, BLACK, (x, y), size // 4)
    # Блик
    circle(surface, WHITE, (x - 2, y - 2), 2)

def draw_nose(surface, x, y):
    '''
    Рисует нос зайца.
    surface - объект pygame.Surface
    x, y - координаты центра носа
    '''
    circle(surface, BLACK, (x, y), 3)

def draw_mouth(surface, x, y):
    '''
    Рисует рот зайца.
    surface - объект pygame.Surface
    x, y - координаты начала рта (от носа)
    '''
    # Левая часть рта
    line(surface, BLACK, (x, y + 3), (x - 5, y + 10), 2)
    # Правая часть рта
    line(surface, BLACK, (x, y + 3), (x + 5, y + 10), 2)

def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует ногу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра ноги
    width, height - ширина и высота ноги
    color - цвет
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_hare(surface, x, y, width, height, main_color, outline_color):
    '''
    Рисует зайца целиком.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - общая ширина и высота изображения
    main_color - основной цвет
    outline_color - цвет контура
    '''
    # Параметры тела
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    
    # Рисуем тело
    draw_body(surface, x, body_y, body_width, body_height, main_color)
    
    # Параметры головы
    head_size = height // 4
    head_y = y - head_size // 2
    
    # Рисуем голову
    draw_head(surface, x, head_y, head_size, main_color)
    
    # Параметры ушей
    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    ear_width = width // 8
    
    # Левое ухо
    ear_x = x - head_size // 4
    draw_ear(surface, ear_x, ear_y, ear_width, ear_height, main_color, outline_color)
    
    # Правое ухо
    ear_x = x + head_size // 4
    draw_ear(surface, ear_x, ear_y, ear_width, ear_height, main_color, outline_color)
    
    # Параметры глаз
    eye_size = head_size // 3
    eye_y = head_y - 5
    eye_offset = head_size // 4
    
    # Левый глаз
    draw_eye(surface, x - eye_offset, eye_y, eye_size)
    
    # Правый глаз
    draw_eye(surface, x + eye_offset, eye_y, eye_size)
    
    # Рисуем нос
    nose_y = head_y + 10
    draw_nose(surface, x, nose_y)
    
    # Рисуем рот
    draw_mouth(surface, x, nose_y)
    
    # Параметры ног
    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    
    # Левая нога
    leg_x = x - width // 4
    draw_leg(surface, leg_x, leg_y, width // 4, leg_height, main_color)
    
    # Правая нога
    leg_x = x + width // 4
    draw_leg(surface, leg_x, leg_y, width // 4, leg_height, main_color)


# Задаем координаты центра и размеры зайца
x, y = 200, 200
width, height = 200, 400

# Рисуем зайца
draw_hare(screen, x, y, width, height, GRAY, DARK_GRAY)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()