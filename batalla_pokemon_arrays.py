import random
import time

player_HP = 100
opponent_HP = 100
player_defense = 100
opponent_defense = 100
opponent_starts = random.randrange(0, 1+1)

player_attack_list = ["malicioso", "placaje", "ascuas"]
player_attack_damage = [0, -35, -10]
player_attack_defense = [-10, 0, 0]
player_attack_effective = [0, 0, -1]

opponent_attack_list = ["látigo", "placaje", "pistola de agua"]
opponent_attack_damage = [0, -30, -40]
opponent_attack_defense = [-10, 0, 0]
opponent_attack_effective = [0, 0, 1]

while player_HP > 0 and opponent_HP > 0:
    if opponent_starts == 0:
        player_attack = input("Opciones: (Malicioso, Placaje, Ascuas)\nAtaque:\n")
        player_attack = player_attack.lower()
    
        try:
            player_attack = player_attack_list.index(player_attack)
        except:
            print("Inserta una de las opciones posibles")
            time.sleep(0.5)
            opponent_starts = 0
            continue
        opponent_HP += player_attack_damage[player_attack] * 100/opponent_defense
        opponent_defense += player_attack_defense[player_attack]
        if opponent_defense <= 0:
            opponent_defense = 1
        if player_attack_effective[player_attack] == -1:
            time.sleep(0.5)
            print("No fue muy efectivo")
        elif player_attack_effective[player_attack] == 1:
            time.sleep(0.5)
            print("Fue super efectivo")

    opponent_starts = 0

    if opponent_HP <= 0:
        break

    time.sleep(0.5)
    opponent_attack = random.randrange(0, 3)
    print("El oponente usó " + opponent_attack_list[opponent_attack])
    
    player_HP += opponent_attack_damage[opponent_attack] * 100/player_defense
    player_defense += opponent_attack_defense[opponent_attack]
    if player_defense <= 0:
        player_attack = 1
    if opponent_attack_effective[opponent_attack] == -1:
        time.sleep(0.5)
        print("No fue muy efectivo")
    elif opponent_attack_effective[opponent_attack] == 1:
        time.sleep(0.5)
        print("Fue super efectivo")
    time.sleep(0.5)

time.sleep(0.5)
if player_HP <= 0:
    print("Has perdido")
else:
    print("Has ganado")