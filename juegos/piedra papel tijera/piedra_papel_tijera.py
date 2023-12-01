import random
import time

def jugar_partida():
    print("Vamos a jugar piedra, papel o tijeras!")
    ordenador = random.choice(["piedra", "papel", "tijeras"])
    jugador = input("Elige piedra, papel o tijeras: ").lower()

    print(f"La computadora eligió {ordenador}.")
    if jugador == ordenador:
        print("Empate!")
        resultado = "han empatado"
    elif jugador == "piedra" and ordenador == "tijeras" or \
            jugador == "papel" and ordenador == "piedra" or \
            jugador == "tijeras" and ordenador == "papel":
        print("Ganaste!")
        resultado = "gana el jugador"
    else:
        print("Perdiste!")
        resultado = "gana el ordenador"
    with open("game_history.txt", "a") as f:
        f.write(
            f"{time.ctime()} - Player: {jugador} vs Computer: {ordenador} - Result: {resultado}\n")
    if input("¿Quieres jugar de nuevo? (s/n) ").lower() == "s":
        jugar_partida()
    else:
        print("Gracias por jugar!")

if __name__ == '__main__':
    jugar_partida()
