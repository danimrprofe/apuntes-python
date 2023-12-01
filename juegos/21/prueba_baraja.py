from carta import Carta
from baraja import Baraja

# Creamos una baraja commpleta (52 cartas)

mibaraja = Baraja()

print("La baraja tiene", mibaraja.contar(), " cartas")

print(mibaraja.quedan_cartas())

# Sacar todas las cartas de la baraja

while mibaraja.quedan_cartas():
    print(mibaraja.sacar_carta(),  " La baraja tiene",
          mibaraja.contar(), " cartas")

mibaraja.barajar()
