def juego_3_en_raya():
    tablero = [" " for x in range(9)]
    turno = "X"
    contador = 0

    def imprimir_tablero():
        row1 = "| {} | {} | {} |".format(tablero[0], tablero[1], tablero[2])
        row2 = "| {} | {} | {} |".format(tablero[3], tablero[4], tablero[5])
        row3 = "| {} | {} | {} |".format(tablero[6], tablero[7], tablero[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    while True:
        imprimir_tablero()
        eleccion = int(
            input("Jugador {} elige una casilla (1-9): ".format(turno)))
        if tablero[eleccion - 1] == " ":
            tablero[eleccion - 1] = turno
            contador += 1
        else:
            print("Casilla ocupada, elige otra.")
            continue
        if contador >= 5:
            if tablero[0] == tablero[1] == tablero[2] != " ":
                print("has ganado")
                break
            if tablero[3] == tablero[4] == tablero[5] != " ":
                print("has ganado")
                break
            if tablero[6] == tablero[7] == tablero[8] != " "  or \
               (tablero[0] == tablero[3] == tablero[6] != " ") or \
               (tablero[1] == tablero[4] == tablero[7] != " ") or \
               (tablero[2] == tablero[5] == tablero[8] != " ") or \
               (tablero[0] == tablero[4] == tablero[8] != " ") or \
               (tablero[2] == tablero[4] == tablero[6] != " "):
                imprimir_tablero()
                print("¡Jugador {} gana!".format(turno))
                break
        if turno == "X":
            turno = "O"
        else:
            turno = "X"

    if input("¿Quieres jugar de nuevo? (s/n)").lower() != "s":
        juego_3_en_raya()

juego_3_en_raya()
