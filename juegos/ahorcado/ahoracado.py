import random

palabras = ['apple', 'mango', 'banana', 'strawberry', 'pineapple']

while True:
    print("Juego del ahorcado\n")
    start = input("Presiona intro para comenzar, o Q para sali: ")
    if start.lower() == 'q':
        break

    palabra_secreta = random.choice(palabras)
    letras_incorrectas = []
    letras_correctas = []

    while len(letras_incorrectas) < 7 and len(letras_correctas) != len(list(palabra_secreta)):

        for letra in palabra_secreta:
            if letra in letras_correctas:
                print(letra, end='')
            else:
                print('_', end='')

        print('')
        print('Intentos: {}/7'.format(len(letras_incorrectas)))
        print('')

        letra_pedida = input("pide una letra: ").lower()

        if len(letra_pedida) != 1:
            print("Solo puedes pedir una letra!")
            continue
        elif letra_pedida in letras_incorrectas or letra_pedida in letras_correctas:
            print("Ya habías pedido esta letra antes")
            continue
        elif not letra_pedida.isalpha():
            print("¡Solo puedes pedir letras!")
            continue

        if letra_pedida in palabra_secreta:
            letras_correctas.append(letra_pedida)
            if len(letras_correctas) == len(list(palabra_secreta)):
                print("¡Has ganado! La letra era {}".format(palabra_secreta))
                break
        else:
            letras_incorrectas.append(letra_pedida)
    else:
        print("No lo has adivinado. La palabra secreta era: {}".format(palabra_secreta))
        break