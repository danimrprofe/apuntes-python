import random

def juego_3_en_raya():
    tablero = [" " for x in range(9)]
    simbolo = "X"
    turno = 0
    MAXIMO_TURNOS = 9
    libres = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def imprimir_tablero():
        print()
        print("| {} | {} | {} |".format(tablero[0], tablero[1], tablero[2]))
        print("| {} | {} | {} |".format(tablero[3], tablero[4], tablero[5]))
        print("| {} | {} | {} |".format(tablero[6], tablero[7], tablero[8]))
        print()

    while turno < MAXIMO_TURNOS:
        imprimir_tablero()

        # Turno del jugador

        eleccion = int(input("Elige una casilla (1-9): ".format(simbolo)))
        posicion = eleccion - 1

        if posicion not in libres:
            print("casilla ", posicion, " no válida")
            continue

        if tablero[posicion] == " ":
            tablero[posicion] = simbolo
            libres.remove(posicion)
            turno += 1
        else:
            print("Casilla ocupada, elige otra.")
            continue

        # No puede haber un ganador antes del quinto simbolo

        if turno >= 5:
            if (tablero[0] == tablero[1] == tablero[2] != " ") or \
               (tablero[3] == tablero[4] == tablero[5] != " ") or \
               (tablero[6] == tablero[7] == tablero[8] != " ") or \
               (tablero[0] == tablero[3] == tablero[6] != " ") or \
               (tablero[1] == tablero[4] == tablero[7] != " ") or \
               (tablero[2] == tablero[5] == tablero[8] != " ") or \
               (tablero[0] == tablero[4] == tablero[8] != " ") or \
               (tablero[2] == tablero[4] == tablero[6] != " "):
                imprimir_tablero()
                print("¡Jugador {} gana!".format(simbolo))
                break

        # Turno del ordenador

        posicion = random.choice(libres)
        print("Ordenador elige casilla ", posicion)
        tablero[posicion] = "O"
        libres.remove(posicion)
        turno += 1

    if input("¿Quieres jugar de nuevo? (s/n)").lower() == "s":
        juego_3_en_raya()

juego_3_en_raya()
