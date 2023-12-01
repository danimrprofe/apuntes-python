class Mano:

    # método constructor
    def __init__(self):
        # Una mano tiene una lista de objetos carta
        self.cartas = []
        self.valor = 0

    # Añadir una carta a la lista
    def añadir_carta(self, carta):
        self.cartas.append(carta)

    def mostrar_mano(self):
        for carta in self.cartas:
            print(carta)

    def calcula_valor(self):
        self.valor = 0
        for carta in self.cartas:
            if carta.valor in ["Reina","Rey","Jota","10"]:
                self.valor += 10
            elif carta.valor == "As":
                self.valor += 11
            else:
                self.valor += int(carta.valor) # 1 <-"1"
