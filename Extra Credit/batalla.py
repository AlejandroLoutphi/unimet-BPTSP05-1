#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande y Ayah ZaherAlDeen

import random
import time
from pokemon import Pokemon, Attack, get_pokemon
from entrenadores import Player, Trainer
from funcs import input_list_elt

def attack(attack: Attack, attacker: Pokemon, victim: Pokemon):
    if random.randint(1, 100) > attack.accuracy:
        print(attacker.name.upper() + " falló")
        return
    if victim.ptype in attack.ptype.strengths:
        time.sleep(0.5)
        print("Fue super efectivo")
        victim.hp -= attack.power * attacker.power // victim.defense * 2
    elif victim.ptype in attack.ptype.weaknesses:
        time.sleep(0.5)
        print("No fue muy efectivo")
        victim.hp -= attack.power * attacker.power // victim.defense // 2
    elif victim.ptype in attack.ptype.inmunes:
        time.sleep(0.5)
        print(victim.name + " es inmune al ataque")
    else:
        victim.hp -= attack.power * attacker.power // victim.defense
    victim.defense *= (100-attack.defense)/100
    victim.defense = max(int(victim.defense), 1)

def display_hps(pkm1: Pokemon, pkm2: Pokemon):
    print("HP de " + pkm1.name.upper() + ": " + str(pkm1.hp))
    print("HP de " + pkm2.name.upper() + ": " + str(pkm2.hp))

def battle(player: Player, opponent: Trainer) -> bool:
    opponent_starts = random.choice([False, True])
    opponent_pkm_id = 0
    print("Un " + opponent.pokemon[opponent_pkm_id].name.upper() + " entra en batalla")

    while True:
        if not opponent_starts:
            display_hps(player.pokemon[0], opponent.pokemon[opponent_pkm_id])
            print('')

            #Tu turno
            chosen_attack = input_list_elt("Es su turno\nAtaques:\n" + '\n'.join([str(i+1) + ') ' + player.pokemon[0].attacks[i].name.upper() for i in range(len(player.pokemon[0].attacks))]) + '\n', [str(i+1) for i in range(len(player.pokemon[0].attacks))])
            attack(player.pokemon[0].attacks[int(chosen_attack)-1], player.pokemon[0], opponent.pokemon[opponent_pkm_id])
        time.sleep(0.5)

        if opponent.pokemon[opponent_pkm_id].hp <= 0:
            print(opponent.pokemon[opponent_pkm_id].name.upper() + " fue derrotado")
            opponent_pkm_id+=1
            try: print("El oponente mandó a " + opponent.pokemon[opponent_pkm_id].name.upper())
            except: pass
        if opponent_pkm_id >= len(opponent.pokemon):
            print("Has ganado")
            player.pokemon[0].level += 1
            if (player.pokemon[0].level % 2)==0 and player.pokemon[0].level < 15: player.pokemon[0].learn_attack()
            player.pokemon[0].power = int(get_pokemon(player.pokemon[0].name).power * 1.01**player.pokemon[0].level)
            player.pokemon[0].defense = int(get_pokemon(player.pokemon[0].name).defense * 1.04**player.pokemon[0].level)
            return True

        display_hps(player.pokemon[0], opponent.pokemon[opponent_pkm_id])
        print('')

        #Turno del oponente
        chosen_attack = random.choice(opponent.pokemon[opponent_pkm_id].attacks)
        print(opponent.pokemon[opponent_pkm_id].name.upper() + " usó " + chosen_attack.name.upper())
        attack(chosen_attack, opponent.pokemon[opponent_pkm_id], player.pokemon[0])
        time.sleep(0.5)

        if player.pokemon[0].hp <= 0:
            print(player.pokemon[0].name.upper() + " fue derrotado")
            print("Has perdido")
            return False

        time.sleep(0.5)
        opponent_starts = False
