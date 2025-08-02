class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=50):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self. felicidad = felicidad
        self. energia = energia
        
    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        self.energia -= 10
        print(f"{self.nombre} jugó y ahora su felicidad es de: {self.felicidad}, su salud esta en: {self.salud}, y su energía en: {self.energia}")
       
    def comer(self):
        self.felicidad += 5
        self.salud += 10
        self.energia += 10 
        print(f"{self.nombre} comió y ahora su felicidad es de: {self.felicidad}, su salud esta en: {self.salud}, y su energía en: {self.energia}")
        
    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        self.energia += 10
        print(f"{self.nombre} se siente mejor y ahora su felicidad es de: {self.felicidad}, su salud esta en: {self.salud}, y su energía en: {self.energia}")