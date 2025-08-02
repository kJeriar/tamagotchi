from tamagotchi import Tamagotchi

class Furawatchi(Tamagotchi):
    def __init__(self, nombre, color="Amarillo floral", salud=100, felicidad=60, energia=60):
        super().__init__(nombre, color, salud, felicidad, energia)
        self.amante_flores = True  # atributo específico de Furawatchi

    def meditar_con_flores(self):
        print(f"{self.nombre} está meditando en la plaza, donde hay muchas flores.... le encanta y lo hace muy felz")
        self.felicidad += 15
        self.energia += 10
        if self.felicidad > 100:
            self.felicidad = 100
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nombre} se siente renovado por que fue a la plaza, su felicidad está puntera en: {self.felicidad}, y su energía esta en lo más alto en: {self.energia}")
