import random
import time

player_HP = 100
opponent_HP = 100
player_defense = 100
opponent_defense = 100
opponent_starts = random.randrange(0, 1+1)

while player_HP > 0 and opponent_HP > 0:
    if opponent_starts == 0:
        player_attack = input("Opciones: (Malicioso, Placaje, Ascuas)\nAtaque:\n")
        player_attack = player_attack.lower()
        if player_attack == "malicioso":
            opponent_defense -= 10
            if opponent_defense <= 0:
                opponent_defense = 1
        elif player_attack == "placaje":
            opponent_HP -= 35 * 100/opponent_defense
        elif player_attack == "ascuas":
            opponent_HP -= 10 * 100/opponent_defense
            time.sleep(0.5)
            print("No fue muy efectivo")
        else:
            print("Inserta una de las opciones posibles")
            time.sleep(0.5)
            opponent_starts = 0
            continue

    opponent_starts = 0

    if opponent_HP <= 0:
        break

    time.sleep(0.5)
    opponent_attack = random.randrange(0, 3)
    if opponent_attack == 0:
        print("El oponente usó látigo")
        player_defense -= 10
        if player_defense <= 0:
            player_defense = 1
    elif opponent_attack == 1:
        print("El oponente usó placaje")
        player_HP -= 30 * 100/player_defense
    else:
        print("El oponente usó pistola de agua")
        player_HP -= 40 * 100/player_defense
        time.sleep(0.5)
        print("Fue super efectivo")
    time.sleep(0.5)

time.sleep(0.5)
if player_HP <= 0:
    print("Has perdido")
else:
    print("Has ganado")