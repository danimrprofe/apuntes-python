```py
import pygame

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ancho_ventana = 640
alto_ventana = 480
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Pelota rebotando")

# Configurar la pelota
color_pelota = (0, 0, 255)  # Azul
radio_pelota = 20
posicion_pelota = [ancho_ventana // 2, alto_ventana // 2]
velocidad_pelota = [5, 5]  # Píxeles por cuadro

# Configurar el reloj
reloj = pygame.time.Clock()

# Bucle de juego
corriendo = True
while corriendo:
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Mover la pelota
    posicion_pelota[0] += velocidad_pelota[0]
    posicion_pelota[1] += velocidad_pelota[1]

    # Rebote en las paredes
    if posicion_pelota[0] - radio_pelota < 0 or posicion_pelota[0] + radio_pelota > ancho_ventana:
        velocidad_pelota[0] = -velocidad_pelota[0]
    if posicion_pelota[1] - radio_pelota < 0 or posicion_pelota[1] + radio_pelota > alto_ventana:
        velocidad_pelota[1] = -velocidad_pelota[1]

    # Dibujar la pelota
    ventana.fill((255, 255, 255))  # Rellenar la ventana con blanco
    pygame.draw.circle(ventana, color_pelota, posicion_pelota, radio_pelota)

    # Actualizar la pantalla
    pygame.display.update()

    # Configurar la velocidad de cuadro
    reloj.tick(60)  # 60 cuadros por segundo

# Salir de Pygame
pygame.quit()

```