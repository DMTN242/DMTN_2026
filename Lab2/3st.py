import pygame

# Инициализация
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Python is AMAZING")

# Цвета
WHITE = (255, 255, 255) #CWET DLA FONA
SKIN = (0, 0, 0)  # NEGR
ORANGE = (255, 100, 0)  # MAIKA
PURPLE = (200, 0, 255)  # VOLOSI
BLUE = (100, 150, 255)  # GLAZA
RED = (255, 50, 50)     # ROT
BLACK = (0, 0, 0)
GREEN = (150, 255, 50)  # TABLO

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Руки 
    pygame.draw.line(screen, SKIN, (300, 450), (220, 250), 20)
    pygame.draw.line(screen, SKIN, (300, 450), (380, 250), 20)

    # Тело 
    pygame.draw.polygon(screen, ORANGE, [(230, 550), (370, 550), (400, 450), (350, 450), (300, 480), (250, 450), (200, 450)])

    # Голова
    pygame.draw.circle(screen, SKIN, (300, 400), 80)
    pygame.draw.circle(screen, BLACK, (300, 400), 80, 2) # Контур

    # Волосы 
    hair_points = [(230, 360), (250, 310), (270, 340), (290, 290), (310, 290), (330, 340), (350, 310), (370, 360)]
    pygame.draw.polygon(screen, PURPLE, hair_points)

    # Глаза
    pygame.draw.circle(screen, BLUE, (270, 385), 15)
    pygame.draw.circle(screen, BLUE, (330, 385), 15)
    pygame.draw.circle(screen, BLACK, (270, 385), 5) # Зрачки
    pygame.draw.circle(screen, BLACK, (330, 385), 5)

    # Нос 
    pygame.draw.polygon(screen, BLACK, [(300, 405), (295, 415), (305, 415)])

    # Рот 
    pygame.draw.polygon(screen, RED, [(260, 430), (340, 430), (300, 470)])

    # Табличка "PYTHON is AMAZING"
    pygame.draw.rect(screen, GREEN, (200, 210, 200, 40))
    pygame.draw.rect(screen, BLACK, (200, 210, 200, 40), 2)
    
    # Текст
    font = pygame.font.SysFont("Arial", 18, bold=True)
    text = font.render("PYTHON is AMAZING", True, BLACK)
    screen.blit(text, (210, 220))

    pygame.display.flip()

pygame.quit()