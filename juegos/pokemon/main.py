from pokemon import Pokemon
from tipoPokemon import TipoPokemon

pikachu = Pokemon("Pikachu", 5, TipoPokemon.ELÉCTRICO, 20, 20, 10, 5)
charmander = Pokemon("Charmander", 5, TipoPokemon.FUEGO, 20, 20, 8, 7)

print(pikachu)
print(charmander)

while not (pikachu.está_derrotado() or charmander.está_derrotado()):
    pikachu.atacar_oponente(charmander)
    print(pikachu.nombre.ljust(15) + charmander.nombre.rjust(15))
    print(str(pikachu.salud_actual).ljust(
        15) + str(charmander.salud_actual).rjust(15))
    print(str(pikachu.ataque).ljust(15) + str(charmander.ataque).rjust(15))
    print(str(pikachu.defensa).ljust(15) + str(charmander.defensa).rjust(15))

    if charmander.está_derrotado():
        break
    charmander.atacar_oponente(pikachu)

if pikachu.está_derrotado():
    print("Pikachu ha sido derrotado.")
else:
    print("Charmander ha sido derrotado.")
