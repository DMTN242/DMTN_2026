import pygame
import math

# Инициализация
pygame.init()
screen = pygame.display.set_mode((1024, 550))
pygame.display.set_caption("PYTHON is REALLY AMAZING!")

# Цвета
WHITE = (255, 255, 255)
SKIN = (243, 203, 178)
DARK_GREEN = (255, 255, 0)
ORANGE = (60, 50, 60)
YELLOW_HAIR = (255, 220, 50)
PURPLE_HAIR = (0, 0, 0)
EYE_BLUE = (124, 185, 232)
EYE_GREY = (175, 192, 173)
RED = (237, 28, 36)
BANNER_GREEN = (127, 255, 0)
BLACK = (0, 0, 0)
GREY = (200, 200, 200) 
FIRE = (255, 69, 0)    
METAL_GREY = (169, 169, 169) # Цвет металлической пластины
BANDANA_COLOR = (40, 40, 40) # Темная ткань

def draw_character(x, y, shirt_color, hair_color, eye_color):
    # Руки
    pygame.draw.line(screen, SKIN, (x - 80, y + 100), (x - 120, y - 200), 20)
    pygame.draw.line(screen, SKIN, (x + 80, y + 100), (x + 120, y - 200), 20)
    
    # Плечи и рукава
    pygame.draw.rect(screen, shirt_color, (x - 100, y + 120, 200, 150))
    pygame.draw.polygon(screen, shirt_color, [(x - 100, y + 120), (x - 160, y + 150), (x - 140, y + 200), (x - 100, y + 200)])
    pygame.draw.polygon(screen, shirt_color, [(x + 100, y + 120), (x + 160, y + 150), (x + 140, y + 200), (x + 100, y + 200)])
    
    # Волосы (теперь за повязкой)
    for i in range(10):
        angle_x = x - 85 + i * 19
        pygame.draw.polygon(screen, hair_color, [(angle_x, y - 50), (angle_x + 10, y - 100), (angle_x + 20, y - 50)])

    # Голова
    pygame.draw.circle(screen, SKIN, (x, y + 50), 110)
    pygame.draw.circle(screen, BLACK, (x, y + 50), 110, 1)

    # --- ПОВЯЗКА НА ЛБУ ---
    # Ткань повязки 
    bandana_rect = pygame.Rect(x - 105, y - 35, 210, 50)
    pygame.draw.rect(screen, BANDANA_COLOR, bandana_rect)
    
    # Металлическая пластина
    metal_rect = pygame.Rect(x - 50, y - 30, 100, 40)
    pygame.draw.rect(screen, METAL_GREY, metal_rect)
    pygame.draw.rect(screen, BLACK, metal_rect, 2) # Контур пластины

    # Спираль на пластине 
    spiral_points = []
    for i in range(100):
        angle = 0.1 * i
        r = 0.15 * i
        px = x + int(r * math.cos(angle))
        py = (y - 10) + int(r * math.sin(angle))
        spiral_points.append((px, py))
    if len(spiral_points) > 1:
        pygame.draw.lines(screen, BLACK, False, spiral_points, 2)

    # Глаза 
    pygame.draw.circle(screen, eye_color, (x - 45, y + 30), 25)
    pygame.draw.circle(screen, BLACK, (x - 45, y + 30), 25, 1)
    pygame.draw.circle(screen, BLACK, (x - 45, y + 30), 6)
    
    pygame.draw.circle(screen, eye_color, (x + 45, y + 30), 25)
    pygame.draw.circle(screen, BLACK, (x + 45, y + 30), 25, 1)
    pygame.draw.circle(screen, BLACK, (x + 45, y + 30), 6)

    # Нос и рот
    pygame.draw.polygon(screen, (100, 50, 0), [(x, y + 80), (x - 10, y + 105), (x + 10, y + 105)])
    pygame.draw.polygon(screen, RED, [(x - 60, y + 130), (x + 60, y + 130), (x, y + 190)])

    # Сигарета
    pygame.draw.line(screen, WHITE, (x + 20, y + 150), (x + 70, y + 160), 6)
    pygame.draw.circle(screen, FIRE, (x + 70, y + 160), 4)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_character(300, 250, DARK_GREEN, YELLOW_HAIR, EYE_GREY)
    draw_character(724, 250, ORANGE, PURPLE_HAIR, EYE_BLUE)

    # Плакат
    pygame.draw.rect(screen, BANNER_GREEN, (30, 80, 960, 80))
    pygame.draw.rect(screen, BLACK, (30, 80, 960, 80), 1)
    font = pygame.font.SysFont("Arial", 54, bold=True)
    text = font.render("PYTHON is REALLY AMAZING!", True, BLACK)
    screen.blit(text, (50, 90))

    pygame.display.flip()

pygame.quit()