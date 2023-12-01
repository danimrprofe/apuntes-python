# 1. elegir palabra

palabra_secreta = "gato"

letras_correctas = []
letras_incorrectas = []

seguir_jugando = True

while seguir_jugando:
    # 2. pintar palabra

    for letra in palabra_secreta:
        if letra in letras_correctas:
            print(letra,end="")
        else:
            print("_ ",end="")

    # 3. pedir letra

    letra_pedida = input("\nDime una letra: \n")

    # 4. determinar letra correcta o no

    if letra_pedida in palabra_secreta:
        letras_correctas.append(letra_pedida)
    else:
        letras_incorrectas.append(letra_pedida)

    print("correctas: ",letras_correctas)
    print("incorrectas: ",letras_incorrectas)

    # Ganar el juego
    if set(letras_correctas) == set(palabra_secreta):
        seguir_jugando = False
        print("HAS GANADO!!")

    # Perder el juego
    if len(letras_incorrectas) == 6:
        seguir_jugando = False
        print("HAS PERDIDO!!")
        print("la palabra era:",palabra_secreta)
