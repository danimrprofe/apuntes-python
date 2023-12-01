import random
from carta import Carta

class Baraja:
    def __init__(self):
        self.cartas = []

        valores = ["As","2","3","4","5","6","7","8","9","10","Jota","Reina","Rey"]
        palos = ["picas","corazones","tréboles","diamantes"]

        for palo in palos:
            for valor in valores:
                cartanueva = Carta(palo, valor)
                self.cartas.append(cartanueva)
    def mezclar(self):
        random.shuffle(self.cartas)
    def contar(self):
        return len(self.cartas)
    def coger_carta(self):
        return self.cartas.pop()
    def mostrar(self):
        for carta in self.cartas:
            print(carta)
