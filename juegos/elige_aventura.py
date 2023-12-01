def iniciar_juego():
    print("¡Bienvenido a la Aventura del Tesoro Perdido!")
    print("Eres un aventurero audaz en busca del tesoro perdido.")
    print("Al comenzar tu viaje, te encuentras con dos caminos.")
    print("Un camino lleva a un bosque denso y el otro a una montaña peligrosa.")
    eleccion = input(
        "¿Quieres ir a la izquierda (bosque) o a la derecha (montaña)? ").lower()
    if eleccion == "izquierda":
        camino_bosque()
    elif eleccion == "derecha":
        camino_montana()
    else:
        print("Elección inválida. Intenta de nuevo.")
        iniciar_juego()


def camino_bosque():
    print("Entras en el bosque denso y te encuentras con un río.")
    print("Puedes seguir el río o cruzarlo.")
    eleccion = input("¿Quieres seguir el río o cruzarlo? ").lower()
    if eleccion == "seguir":
        print("Sigues el río y te encuentras con una cascada oculta.")
        print("Detrás de la cascada, encuentras una pequeña cueva.")
        print("Entras en la cueva y encuentras el tesoro perdido!")
        print("¡Felicidades, has completado tu misión!")
    elif eleccion == "cruzar":
        print("Intentas cruzar el río pero caes en las corrientes.")
        print("Eres arrastrado y pierdes todos tus suministros.")
        print(
            "Desafortunadamente, tienes que dar media vuelta y comenzar tu viaje de nuevo.")
        iniciar_juego()
    else:
        print("Elección inválida. Intenta de nuevo.")
        camino_bosque()


def camino_montana():
    print("Comienzas a escalar la montaña peligrosa.")
    print("A medida que subes, el camino se vuelve más estrecho y peligroso.")
    print("Te encuentras con una bifurcación en el camino.")
    print("Un camino lleva a la cima de la montaña y el otro a un acantilado.")
    eleccion = input(
        "¿Quieres ir a la izquierda (cima) o a la derecha (acantilado)? ").lower()
    if eleccion == "izquierda":
        print("Llegas a la cima de la montaña y encuentras el tesoro perdido!")
        print("¡Felicidades, has completado tu misión!")
    elif eleccion == "derecha":
        print("Te acercas demasiado al acantilado y pierdes el equilibrio.")
        print("Caes al vacío y desafortunadamente pierdes la vida.")
        print(
            "Desafortunadamente, tienes que dar media vuelta y comenzar tu viaje de nuevo.")
        iniciar_juego()
    else:
        print("Elección inválida. Intenta de nuevo.")
        camino_montana()


iniciar_juego()
