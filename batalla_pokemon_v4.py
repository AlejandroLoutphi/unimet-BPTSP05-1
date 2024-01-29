import random
import time

#Inicialización; parámetros de los ataques
#Las tuplas contienen HP, Defensa y Mensajes respectivamente
player_values = 100, 100
opponent_values = 100, 100
opponent_starts = random.randrange(0, 1+1)

attack_values = {
    "malicioso": (0, -10, None), 
    "placaje": (-35, 0, None), 
    "ascuas": (-10, 0, "No fue muy efectivo"),
    "látigo": (-10, -10, None),
    "pistola de agua": (-40, 0, "Fue super efectivo")
}

#Main loop
while True:
    if opponent_starts == 0:
        #Tu turno
        x = input("Opciones: (Malicioso, Placaje, Ascuas)\nAtaque:\n")
        x = x.lower()
    
        if x in ["malicioso", "placaje", "ascuas"]:
            if attack_values[x][2] is not None:
                time.sleep(0.5)
                print(attack_values[x][2])
            opponent_values = (opponent_values[0] + attack_values[x][0] * 100/opponent_values[1]), max(1, opponent_values[1] + attack_values[x][1])
            if opponent_values[0] <= 0:
                break
        else:
            print("Inserta una de las opciones posibles")
            time.sleep(0.5)
            continue

    time.sleep(0.5)

    #Turno del oponente
    x = random.choice(["látigo", "placaje", "pistola de agua"])
    print("El oponente usó " + x)
    if attack_values[x][2] is not None:
        time.sleep(0.5)
        print(attack_values[x][2])
    player_values = (player_values[0] + attack_values[x][0] * 100/player_values[1]), max(1, player_values[1] + attack_values[x][1])
    if player_values[0] <= 0:
        break

    time.sleep(0.5)
    opponent_starts = 0

#Fin de la batalla
time.sleep(0.5)
if player_values[0] <= 0:
    print("Has perdido")
else:
    print("Has ganado")