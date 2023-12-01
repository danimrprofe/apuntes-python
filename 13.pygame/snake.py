import pygame
import time

# Inicializar Pygame
pygame.init()

# Crear ventana del juego
win = pygame.display.set_mode((500, 500))

# Crear título de la ventana
pygame.display.set_caption("Snake Game")

# Variables del juego
x = 50
y = 50
width = 10
height = 10
vel = 10

# Bucle principal del juego
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Mover la serpiente
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # Pintar la ventana
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
