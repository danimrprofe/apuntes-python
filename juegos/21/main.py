from baraja import Baraja
from mano import Mano


class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.baraja.barajar()

    def infomano(self, mano):
        print("Mano de ", mano.nombre_jugador, "es: ", mano.cartas,
              "lo que hace un total de: ", mano.calcular_valor())

    def jugar(self):
        mano_jugador = Mano("Dani")
        mano_PC = Mano("PC")
        mano_jugador.añadir_carta(self.baraja.sacar_carta())
        mano_PC.añadir_carta(self.baraja.sacar_carta())

        self.infomano(mano_jugador)
        self.infomano(mano_PC)
        while mano_jugador.valor < 21:
            action = input("Quieres PEDIR carta o PASAR? ").lower()
            if action == "pedir":
                cartanueva = self.baraja.sacar_carta()
                print(mano_jugador.nombre_jugador, "recibe un ", cartanueva)
                mano_jugador.añadir_carta(cartanueva)
                if mano_jugador.valor < 21:
                    cartanueva = self.baraja.sacar_carta()
                    print(mano_PC.nombre_jugador, "recibe un ", cartanueva)
                    self.infomano(mano_jugador)
                    self.infomano(mano_PC)
            else:
                if mano_PC.calcular_valor() <= mano_jugador.calcular_valor():
                    mano_PC.añadir_carta(self.baraja.sacar_carta())
                else:
                    print("Tu puntuación final es de",
                          mano_jugador.calcular_valor())
                    print("Puntuación PC",
                          mano_PC.calcular_valor())
                    return
        if mano_jugador.valor == 21:
            print("has GANADO.")
        else:
            print("has PERDIDO.")
        print("Tu puntuación final es de",
              mano_jugador.calcular_valor())


if __name__ == '__main__':
    print("hola")
    juego = Juego()
    juego.jugar()
