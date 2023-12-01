import random

print("Vamos a jugar un juego de adivinanza!")
numero = random.randint(1, 100)
intentos = 0
while True:
    adivinanza = int(input("Adivine un número entre 1 y 100: "))
    intentos += 1
    if adivinanza == numero:
        print(f"Adivinaste en {intentos} intentos!")
        break
    elif adivinanza < numero:
        print("Demasiado bajo, inténtalo de nuevo.")
    else:
        print("Demasiado alto, inténtalo de nuevo.")
