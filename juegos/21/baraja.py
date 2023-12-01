import random
from carta import Carta

class Baraja:
    def __init__(self):
        self.cartas = []
        palos = ["♥", "♦", "♣", "♠"]
        valores = ["As", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Jota", "Reina", "Rey"]
        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo, valor))

    def barajar(self):
        random.shuffle(self.cartas)

    def __repr__(self):
        return f"Baraja de {self.contar()} cartas"

    def contar(self):
        return len(self.cartas)

    def sacar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return None

    def quedan_cartas(self):
        """Devuelve True si quedan cartas en la baraja, False si no."""
        return len(self.cartas) != 0

    def mostrar_cartas(self):
        for carta in self.cartas:
            print(carta)
