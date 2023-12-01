
palabra_secreta = "patata"
#letras_correctas = ["p","t","t","a","a","a"]
letras_correctas = []
letras_incorrectas = []

print("Juego del ahorcado")

longitud_palabra = len(palabra_secreta)

# _ _ _ _ _ _

while longitud_palabra > 0:
    print("_ ", end="")
    longitud_palabra = longitud_palabra -1

letra_pedida = input("pide una letra")

# p a t a t a
for letra in palabra_secreta:
    if letra == letra_pedida:
        print(letra, end="")
        letras_correctas.append(letra)
    else:
        print("_", end="")
        letras_incorrectas.append(letra)
