import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Angry Emoji")

# Цвета
GRAY = (211, 211, 211)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRAY)

    # Лицо
    pygame.draw.circle(screen, YELLOW, (200, 200), 100)
    pygame.draw.circle(screen, BLACK, (200, 200), 100, 1) # Тонкий контур

    # Красные глаза с черными зрачками
    # Левый
    pygame.draw.circle(screen, RED, (160, 180), 18)
    pygame.draw.circle(screen, BLACK, (160, 180), 6)
    # Правый
    pygame.draw.circle(screen, RED, (240, 180), 18)
    pygame.draw.circle(screen, BLACK, (240, 180), 6)

    # Брови (толстые наклонные линии)
    pygame.draw.line(screen, BLACK, (120, 120), (185, 170), 12) # Левая
    pygame.draw.line(screen, BLACK, (280, 140), (215, 175), 12) # Правая

    # Рот (черный прямоугольник)
    # rect: [отступ слева, отступ сверху, ширина, высота]
    pygame.draw.rect(screen, BLACK, (150, 250, 100, 20))

    pygame.display.flip()

pygame.quit()