# Esta clase define el objeto Mano, el cual representa un conjunto de cartas.
class Mano:

    # El método __init__ establece la lista de cartas como una lista vacía y el valor como 0.
    def __init__(self, nombre):
        self.cartas = []
        self.valor = 0
        self.nombre_jugador = nombre

    # El método añadir_carta añade una carta a la lista de cartas.
    def añadir_carta(self, carta):
        self.cartas.append(carta)

    # El método calcular_valor calcula el valor de todas las cartas en la mano. Si el valor de la carta es Jota, Reina o Rey, el valor se asigna como 10. Si el valor de la carta es As, se asigna el valor 11 y se establece la variable has_ace como True. En cualquier otro caso, el valor se asigna como el valor entero de la carta.
    def calcular_valor(self):
        self.valor = 0

        for carta in self.cartas:
            if carta.valor in ["Jota", "Reina", "Rey"]:
                self.valor += 10
            elif carta.valor == "As":

                self.valor += 11
            else:
                self.valor += int(carta.valor)

        return self.valor

    def mostrar_mano(self):
        for carta in self.cartas:
            print(carta)
