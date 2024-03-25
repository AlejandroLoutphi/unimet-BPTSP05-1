#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande y Ayah ZaherAlDeen

import time
from funcs import input_list_elt
from funcs import input_posint
from entrenadores import Player, Trainer
from pokemon import get_pokemon
from batalla import battle
from ubicaciones import Location, Town, League

def input_player_and_rival() -> tuple[Player, Trainer]:
    gender = input_list_elt("¿Eres:\n1) Chico, o\n2) Chica\n?\n", ['1', '2'])
    if gender == "1": gender = 'o'
    else: gender = 'a'
    print("Bienvenid" + gender + " al mundo de los Pokémon")

    name = input("¿Cuál es tu nombre?\n")

    age = input_posint("¿Qué edad tienes?\n")
    if age < 10:
        print("No tienes edad para ser entrenador" + 'a'*(gender=='a'))
        quit()
    else:
        print("Vamos!")

    region = input("Necesitarás un compañero de viaje.\n¿En qué región te encuentras?\n(Sugerencia: Kanto)\n")
    region = region.lower()
    if region == "kanto" and gender == 'o':
        print("Tu compañera de viaje es Misty")
        rival = "Misty"
    else:
        print("Tu compañero de viaje es Brock")
        rival = "Brock"
    return (Player(name, gender, age, region), Trainer(rival))

def pick_starter(player: Player, rival: Trainer):
    starter = input_list_elt("¿Qué Pokémon quieres para empezar?\n1) Bulbasaur\n2) Charmander\n3) Squirtle\n", ['1','2','3'])

    if starter == "1":
        print("Tu starter es Bulbasaur")
        player.pokemon.append(get_pokemon("bulbasaur"))
        rival.pokemon.append(get_pokemon("charmander"))
    elif starter == "2":
        print("Tu starter es Charmander")
        player.pokemon.append(get_pokemon("charmander"))
        rival.pokemon.append(get_pokemon("squirtle"))
    else:
        print("Tu starter es Squirtle")
        player.pokemon.append(get_pokemon("squirtle"))
        rival.pokemon.append(get_pokemon("bulbasaur"))

def intro_sequence() -> Player:
    player, rival = input_player_and_rival()
    pick_starter(player, rival)

    time.sleep(0.5)
    print('')

    print(rival.name + ": Te reto a una batalla pokemon.")
    
    time.sleep(0.5)
    print('')

    x = battle(player, rival)
    if x: print(rival.name + ": Te ganaré la próxima vez.")
    else: print(rival.name + ": Sabía que te ganaría.")
    return player

def main():
    player = intro_sequence()
    locations = [
        Town("Pueblo Rojo", [get_pokemon("rattata"), get_pokemon("pidgey")]),
        Location("Ruta 1", [get_pokemon("rattata")]),
        Location("Ruta 2", [get_pokemon("caterpie")]),
        Town("Pueblo Naranja", [get_pokemon("caterpie"), get_pokemon("pidgey")]),
        Location("Ruta 3",[get_pokemon("pidgey")]),
        Location("Ruta 4",[get_pokemon("bellsprout")]),
        Town("Pueblo Amarillo",[get_pokemon("bellsprout"),get_pokemon("rattata")]),
        Location("Ruta 5",[get_pokemon("mankey")]),
        Location("Ruta 6",[get_pokemon("geodude")]),
        Town("Pueblo Azul",[get_pokemon("mankey"),get_pokemon("geodude")]),
        Location("Ruta 7", [get_pokemon("drowzee")]),
        Location("Ruta 8", [get_pokemon("snorlax")]),
        Town("Pueblo Verde",[get_pokemon("drowzee"),get_pokemon("tentacool")]),
        Location("Ruta 9", [get_pokemon("tentacool")]),
        Location("Ruta 10", [get_pokemon("ekans")]),
        Town("Pueblo Morado", [get_pokemon("snorlax"), get_pokemon("tentacool")]),
        Location("Ruta 11", [get_pokemon("pikachu")]),
        Location("Ruta 12", [get_pokemon("tentacool")]),
        Town("Pueblo Indigo", [get_pokemon("ekans"), get_pokemon("haunter")]),
        Location("Ruta 13", [get_pokemon("dugtrio")]),
        Location("Ruta 14", [get_pokemon("haunter")]),
        League("Liga", [get_pokemon("tentacool"), get_pokemon("haunter"), get_pokemon("dugtrio")]),
        ]
    active = 0
    while True:
        next = locations[active].menu(player)
        if next: active+=1
        else: active-=1
        active = max(active, 0)

main()