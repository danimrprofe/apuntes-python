import random


def combate_pokemon(nombre_pokemon1, nombre_pokemon2):
    vida_pokemon1 = 100
    vida_pokemon2 = 100
    print("¡Comienza el combate entre {} y {}!".format(
        nombre_pokemon1, nombre_pokemon2))
    while vida_pokemon1 > 0 and vida_pokemon2 > 0:
        ataque_pokemon1 = random.randint(10, 30)
        vida_pokemon2 -= ataque_pokemon1
        print("{} ataca a {}, causando un daño de {} puntos. Vida de {}: {}".format(
            nombre_pokemon1, nombre_pokemon2, ataque_pokemon1, nombre_pokemon2, vida_pokemon2))
        if vida_pokemon2 <= 0:
            break
        ataque_pokemon2 = random.randint(10, 30)
        vida_pokemon1 -= ataque_pokemon2
        print("{} ataca a {}, causando un daño de {} puntos. Vida de {}: {}".format(
            nombre_pokemon2, nombre_pokemon1, ataque_pokemon2, nombre_pokemon1, vida_pokemon1))
    if vida_pokemon1 > 0:
        print("{} gana el combate contra {}!".format(
            nombre_pokemon1, nombre_pokemon2))
    else:
        print("{} gana el combate contra {}!".format(
            nombre_pokemon2, nombre_pokemon1))


combate_pokemon("Pikachu", "Charmander")
