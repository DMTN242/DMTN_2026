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

# Задаем координаты центра и размеры зайца
x, y = 200, 200  
width, height = 200, 400  

# Рисуем тело
body_width = width // 2  
body_height = height // 2  
body_y = y + body_height // 2  
'''
Рисует тело зайца.
screen - объект pygame.Surface
x, body_y - координаты центра тела
body_width, body_height - ширина и высота тела
GRAY - цвет
'''
ellipse(screen, GRAY, (x - body_width // 2, body_y - body_height // 2, body_width, body_height))

# Рисуем голову
head_size = height // 4  
head_y = y - head_size // 2  
'''
Рисует голову зайца.
screen - объект pygame.Surface
x, head_y - координаты центра головы
head_size // 2 - радиус головы
GRAY - цвет
'''
circle(screen, GRAY, (x, head_y), head_size // 2)

# Задаем параметры ушей
ear_height = height // 3  
ear_y = y - height // 2 + ear_height // 2  
ear_width = width // 8  

# Левое ухо
ear_x = x - head_size // 4  
'''
Рисует основную часть левого уха.
screen - объект pygame.Surface
ear_x, ear_y - координаты центра уха
ear_width, ear_height - ширина и высота уха
GRAY - цвет
'''
ellipse(screen, GRAY, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height))
'''
Рисует контур левого уха.
screen - объект pygame.Surface
ear_x, ear_y - координаты центра контура
ear_width, ear_height - ширина и высота контура
DARK_GRAY - цвет контура
Толщина линии - 2 пикселя
'''
ellipse(screen, DARK_GRAY, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height), 2)

# Правое ухо
ear_x = x + head_size // 4  
'''
Рисует основную часть правого уха.
screen - объект pygame.Surface
ear_x, ear_y - координаты центра уха
ear_width, ear_height - ширина и высота уха
GRAY - цвет
'''
ellipse(screen, GRAY, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height))
'''
Рисует контур правого уха.
screen - объект pygame.Surface
ear_x, ear_y - координаты центра контура
ear_width, ear_height - ширина и высота контура
DARK_GRAY - цвет контура
Толщина линии - 2 пикселя
'''
ellipse(screen, DARK_GRAY, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height), 2)

# Задаем параметры глаз
eye_size = head_size // 3  
eye_y = head_y - 5  
eye_offset = head_size // 4  

# Левый глаз
eye_x = x - eye_offset  
'''
Рисует белок левого глаза.
screen - объект pygame.Surface
eye_x, eye_y - координаты центра белка
eye_size // 2 - радиус белка
WHITE - цвет
'''
circle(screen, WHITE, (eye_x, eye_y), eye_size // 2)
'''
Рисует зрачок левого глаза.
screen - объект pygame.Surface
eye_x, eye_y - координаты центра зрачка
eye_size // 4 - радиус зрачка
BLACK - цвет
'''
circle(screen, BLACK, (eye_x, eye_y), eye_size // 4)
'''
Рисует блик в левом глазу.
screen - объект pygame.Surface
eye_x - 2, eye_y - 2 - координаты центра блика
2 - радиус блика
WHITE - цвет
'''
circle(screen, WHITE, (eye_x - 2, eye_y - 2), 2)

# Правый глаз
eye_x = x + eye_offset  
'''
Рисует белок правого глаза.
screen - объект pygame.Surface
eye_x, eye_y - координаты центра белка
eye_size // 2 - радиус белка
WHITE - цвет
'''
circle(screen, WHITE, (eye_x, eye_y), eye_size // 2)
'''
Рисует зрачок правого глаза.
screen - объект pygame.Surface
eye_x, eye_y - координаты центра зрачка
eye_size // 4 - радиус зрачка
BLACK - цвет
'''
circle(screen, BLACK, (eye_x, eye_y), eye_size // 4)
'''
Рисует блик в правом глазу.
screen - объект pygame.Surface
eye_x - 2, eye_y - 2 - координаты центра блика
2 - радиус блика
WHITE - цвет
'''
circle(screen, WHITE, (eye_x - 2, eye_y - 2), 2)

# Рисуем нос
nose_y = head_y + 10  
'''
Рисует нос зайца.
screen - объект pygame.Surface
x, nose_y - координаты центра носа
3 - радиус носа
BLACK - цвет
'''
circle(screen, BLACK, (x, nose_y), 3)

# Рисуем рот
'''
Рисует левую часть рта.
screen - объект pygame.Surface
(x, nose_y + 3) - начальная точка линии
(x - 5, nose_y + 10) - конечная точка линии
2 - толщина линии
BLACK - цвет
'''
line(screen, BLACK, (x, nose_y + 3), (x - 5, nose_y + 10), 2)
'''
Рисует правую часть рта.
screen - объект pygame.Surface
(x, nose_y + 3) - начальная точка линии
(x + 5, nose_y + 10) - конечная точка линии
2 - толщина линии
BLACK - цвет
'''
line(screen, BLACK, (x, nose_y + 3), (x + 5, nose_y + 10), 2)

# Рисуем ноги
leg_height = height // 16  
leg_y = y + height // 2 - leg_height // 2  

# Левая нога
leg_x = x - width // 4  
'''
Рисует левую ногу зайца.
screen - объект pygame.Surface
leg_x, leg_y - координаты центра ноги
width // 4, leg_height - ширина и высота ноги
GRAY - цвет
'''
ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))

# Правая нога
leg_x = x + width // 4  
'''
Рисует правую ногу зайца.
screen - объект pygame.Surface
leg_x, leg_y - координаты центра ноги
width // 4, leg_height - ширина и высота ноги
GRAY - цвет
'''
ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))

pygame.display.update()  
clock = pygame.time.Clock()  
finished = False  

while not finished:  
    clock.tick(FPS)  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            finished = True  

pygame.quit()  