class Persona:
    def __init__ (self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self. tamagotchi = tamagotchi
    
    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} {self.apellido} juega con {self.tamagotchi.nombre}")
        self.tamagotchi.jugar()
        
    def darle_comida(self):
        print(f"{self.nombre} {self.apellido} le da comidita a {self.tamagotchi.nombre}")
        self.tamagotchi.comer()

    def curarlo(self):
        print(f"{self.nombre} {self.apellido} mejora a {self.tamagotchi.nombre}")
        self.tamagotchi.curar()
    