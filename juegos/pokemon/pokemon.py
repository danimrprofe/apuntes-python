
class Pokemon:
    def __init__(self, nombre, nivel, tipo, salud_maxima, salud_actual, ataque, defensa):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.salud_maxima = salud_maxima
        self.salud_actual = salud_actual
        self.ataque = ataque
        self.defensa = defensa

    def __repr__(self):
        return f"{self.nombre} (Nivel {self.nivel} Pokemon {self.tipo.value})\nSalud: {self.salud_actual}/{self.salud_maxima}\nAtaque: {self.ataque}\nDefensa: {self.defensa}"

    def atacar_oponente(self, oponente):
        daño = self.ataque - oponente.defensa
        if daño <= 0:
            daño = 1
        oponente.salud_actual -= daño
        print(f"{self.nombre} atacó a {oponente.nombre} por {daño} de daño!")
        if oponente.está_derrotado():
            print(f"{oponente.nombre} ha sido derrotado!")

    def está_derrotado(self):
        return self.salud_actual <= 0
