import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Цвета
GRAY = (180, 180, 180)
DARK_GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

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

def draw_ear(surface, x, y, width, height, color, outline_color, inner_color):
    '''
    Рисует ухо зайца.
    surface - объект pygame.Surface
    x, y - координаты центра уха
    width, height - ширина и высота уха
    color - основной цвет
    outline_color - цвет контура
    inner_color - цвет внутренней части
    '''
    # Основное ухо
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    # Контур
    ellipse(surface, outline_color, (x - width // 2, y - height // 2, width, height), 2)
    # Внутренняя розовая часть
    ellipse(surface, inner_color, (x - width // 4, y - height // 4, width // 2, height // 2))

def draw_eye(surface, x, y, size):
    '''
    Рисует глаз зайца.
    surface - объект pygame.Surface
    x, y - координаты центра глаза
    size - диаметр глаза
    '''
    # Белок
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
    line(surface, BLACK, (x, y + 3), (x - 5, y + 10), 2)
    line(surface, BLACK, (x, y + 3), (x + 5, y + 10), 2)

def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует ногу/лапу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра ноги
    width, height - ширина и высота ноги
    color - цвет
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_hare(surface, x, y, width, height, color):
    '''
    Рисует зайца на экране.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изображения
    color - основной цвет
    '''
    # Параметры частей тела
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    
    head_size = height // 4
    head_y = y - head_size // 2
    
    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    ear_width = width // 8
    
    eye_size = head_size // 3
    eye_y = head_y - 5
    eye_offset = head_size // 4
    
    nose_y = head_y + 10
    
    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    
    # Рисуем тело
    draw_body(surface, x, body_y, body_width, body_height, color)
    
    # Рисуем уши
    ear_x_left = x - head_size // 4
    draw_ear(surface, ear_x_left, ear_y, ear_width, ear_height, color, DARK_GRAY, PINK)
    
    ear_x_right = x + head_size // 4
    draw_ear(surface, ear_x_right, ear_y, ear_width, ear_height, color, DARK_GRAY, PINK)
    
    # Рисуем голову
    draw_head(surface, x, head_y, head_size, color)
    
    # Рисуем глаза
    draw_eye(surface, x - eye_offset, eye_y, eye_size)
    draw_eye(surface, x + eye_offset, eye_y, eye_size)
    
    # Рисуем нос
    draw_nose(surface, x, nose_y)
    
    # Рисуем рот
    draw_mouth(surface, x, nose_y)
    
    # Рисуем ноги (нижние)
    leg_x_left = x - width // 4
    draw_leg(surface, leg_x_left, leg_y, width // 4, leg_height, color)
    
    leg_x_right = x + width // 4
    draw_leg(surface, leg_x_right, leg_y, width // 4, leg_height, color)
    
    # Рисуем лапы (верхние)
    leg_y_upper = y + leg_height // 2
    draw_leg(surface, leg_x_left, leg_y_upper, width // 4, leg_height, color)
    draw_leg(surface, leg_x_right, leg_y_upper, width // 4, leg_height, color)


# Рисуем зайца
draw_hare(screen, 200, 200, 200, 400, GRAY)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()