#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande y Ayah ZaherAlDeen

import time
import random
import copy
from funcs import input_list_elt
from entrenadores import Trainer
from pokemon import get_pokemon
from batalla import battle

class Location:
    def __init__(self, name: str, pokemon: list):
        self.name = name
        self.pokemon = pokemon
    def menu(self, player) -> bool:
        print(self.name)
        if random.choice([True, False]) and player.pokemon[0].hp > 0:
            print("Un pokemón salvaje ha aparecido")
            loc_pkm = copy.deepcopy(self).pokemon
            battle(player, Trainer("Pokemón Salvaje", loc_pkm))
        x = input_list_elt("Opciones:\n1) Ir al siguiente lugar\n2) Volver al lugar anterior\n", ['1', '2'])
        if x=='1': return True
        else: return False

class Town(Location):
    def menu(self, player) -> bool:
        print(self.name)
        while True:
            x = input_list_elt("Opciones:\n1) Curar Pokemon\n2) Enfrentar al lider\n3) Ir al siguiente lugar\n4) Volver al lugar anterior\n", ['1', '2', '3', '4'])
            if x=='1':
                player.pokemon[0].hp = int(get_pokemon(player.pokemon[0].name).hp * 1.04**player.pokemon[0].level)
                player.pokemon[0].power = int(get_pokemon(player.pokemon[0].name).power * 1.01**player.pokemon[0].level)
                player.pokemon[0].defense = int(get_pokemon(player.pokemon[0].name).defense * 1.04**player.pokemon[0].level)
                print("Pokemon curado")
            elif x=='2':
                if player.pokemon[0].hp > 0:
                    loc_pkm = copy.deepcopy(self).pokemon
                    y = battle(player, Trainer("Líder de " + self.name, loc_pkm))
                    if y: player.badges = list(set(player.badges + [self.name]))
                else: print("No puede enfrentar al líder con un pokemón desmayado")
            elif x=='3': return True
            else: return False

class League(Location):
    def menu(self, player) -> bool:
        print(self.name)
        while True:
            if len(player.badges) == 7: x = input_list_elt("Opciones:\n1) Curar Pokemon\n2) Volver al lugar anterior\n3) Enfrentar al lider de la liga\n", ['1', '2', '3'])
            else:
                print("Necesitas derrotar a los líderes de los 7 pueblos para desafíar al líder de la liga")
                x = input_list_elt("Opciones:\n1) Curar Pokemon\n2) Volver al lugar anterior\n", ['1', '2'])
            if x=='1':
                player.pokemon[0].hp = int(get_pokemon(player.pokemon[0].name).hp * 1.04**player.pokemon[0].level)
                player.pokemon[0].power = int(get_pokemon(player.pokemon[0].name).power * 1.01**player.pokemon[0].level)
                player.pokemon[0].defense = int(get_pokemon(player.pokemon[0].name).defense * 1.04**player.pokemon[0].level)
                print("Pokemon curados")
            elif x=='3':
                if player.pokemon[0].hp > 0:
                    loc_pkm = copy.deepcopy(self).pokemon
                    y = battle(player, Trainer("Líder de " + self.name, loc_pkm))
                    if y:
                        print("Ha derrotado el líder de la liga")
                        time.sleep(0.5)
                        print("¡Bien Hecho! ¡Has Ganado!")
                        input("Presione Enter para continuar")
                        quit()
                else: print("No puede enfrentar al líder con un pokemón desmayado")
            else: return False