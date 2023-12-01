import random


def iniciar_juego():
    print("Vamos a jugar un juego de adivinanza!")
    numero = random.randint(1, 100)
    intentos = 0
    adivinanza = None
    while adivinanza != numero:
        adivinanza = int(input("Adivine un número entre 1 y 100: "))
        intentos += 1
        if adivinanza == numero:
            print(f"Adivinaste en {intentos} intentos!")
        elif adivinanza < numero:
            print("Demasiado bajo, inténtalo de nuevo.")
        else:
            print("Demasiado alto, inténtalo de nuevo.")
    play_again = input("¿Quieres jugar de nuevo? (s/n) ").lower()
    if play_again == 's':
        iniciar_juego()
    else:
        print("Gracias por jugar!")


if __name__ == '__main__':
    iniciar_juego()
50
