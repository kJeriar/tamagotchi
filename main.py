from persona import Persona
from tamagotchi import Tamagotchi
from furawatchi import Furawatchi

mi_tamagotchi = Tamagotchi(nombre="kuku", color="rojo")
creando_furacito = Furawatchi(nombre="Furacito")

Pedro = Persona(nombre="Pedro", apellido="Paramo", tamagotchi=creando_furacito)

persona = Persona(nombre = "Karla", apellido ="Jeria", tamagotchi = mi_tamagotchi)

persona.darle_comida()
persona.curarlo()
persona.jugar_con_tamagotchi()

creando_furacito.meditar_con_flores()