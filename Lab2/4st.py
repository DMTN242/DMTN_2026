import pygame

# Инициализация
pygame.init()
screen = pygame.display.set_mode((1024, 550))
pygame.display.set_caption("PYTHON is REALLY AMAZING!")

# Цвета
WHITE = (255, 255, 255)
SKIN = (243, 203, 178)
DARK_GREEN = (0, 114, 0)
ORANGE = (255, 102, 0)
YELLOW_HAIR = (255, 220, 50)
PURPLE_HAIR = (191, 0, 255)
EYE_BLUE = (124, 185, 232)
EYE_GREY = (175, 192, 173)
RED = (237, 28, 36)
BANNER_GREEN = (127, 255, 0)
BLACK = (0, 0, 0)


def draw_character(x, y, shirt_color, hair_color, eye_color):
    # Руки 
    pygame.draw.line(screen, SKIN, (x - 80, y + 100), (x - 120, y - 200), 20)
    pygame.draw.line(screen, SKIN, (x + 80, y + 100), (x + 120, y - 200), 20)
    # Плечи 
    pygame.draw.rect(screen, shirt_color, (x - 100, y + 120, 200, 150))
    # Рукава
    pygame.draw.polygon(screen, shirt_color, [(x - 100, y + 120), (x - 160, y + 150), (x - 140, y + 200), (x - 100, y + 200)])
    pygame.draw.polygon(screen, shirt_color, [(x + 100, y + 120), (x + 160, y + 150), (x + 140, y + 200), (x + 100, y + 200)])
    
    # Волосы (колючки)
    for i in range(10):
        angle_x = x - 85 + i * 19
        pygame.draw.polygon(screen, hair_color, [(angle_x, y - 50), (angle_x + 10, y - 100), (angle_x + 20, y - 50)])

    # Голова
    pygame.draw.circle(screen, SKIN, (x, y + 50), 110)
    pygame.draw.circle(screen, BLACK, (x, y + 50), 110, 1) # Контур
    
    # Глаза
    pygame.draw.circle(screen, eye_color, (x - 45, y + 30), 25)
    pygame.draw.circle(screen, BLACK, (x - 45, y + 30), 25, 1)
    pygame.draw.circle(screen, BLACK, (x - 45, y + 30), 6) # Зрачок
    
    pygame.draw.circle(screen, eye_color, (x + 45, y + 30), 25)
    pygame.draw.circle(screen, BLACK, (x + 45, y + 30), 25, 1)
    pygame.draw.circle(screen, BLACK, (x + 45, y + 30), 6) # Зрачок

    # Нос 
    pygame.draw.polygon(screen, (100, 50, 0), [(x, y + 80), (x - 10, y + 105), (x + 10, y + 105)])
    
    # Рот 
    pygame.draw.polygon(screen, RED, [(x - 60, y + 130), (x + 60, y + 130), (x, y + 190)])

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Отрисовка двух персонажей
    draw_character(300, 250, DARK_GREEN, YELLOW_HAIR, EYE_GREY)
    draw_character(724, 250, ORANGE, PURPLE_HAIR, EYE_BLUE)

    # Плакат
    pygame.draw.rect(screen, BANNER_GREEN, (30, 80, 960, 80))
    pygame.draw.rect(screen, BLACK, (30, 80, 960, 80), 1)

    # Текст на плакате
    font = pygame.font.SysFont("Arial", 54, bold=True)
    text = font.render("PYTHON is REALLY AMAZING!", True, BLACK)
    screen.blit(text, (50, 90))

    pygame.display.flip()

pygame.quit()