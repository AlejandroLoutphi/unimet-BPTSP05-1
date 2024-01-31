import random
import time

def attack(attack, opponent):
    if attack[2] is not None:
        time.sleep(0.5)
        print(attack[2])
    return (opponent[0] + attack[0] * 100/opponent[1]), max(1, opponent[1] + attack[1])

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

player_attacks = ["malicioso", "placaje", "ascuas"]
opponent_attacks = ["látigo", "placaje", "pistola de agua"]

#Main loop
while True:
    if opponent_starts == 0:
        #Tu turno
        x = input("Opciones: (Malicioso, Placaje, Ascuas)\nAtaque:\n")
        x = x.lower()
    
        if x in player_attacks:
            opponent_values = attack(attack_values[x], opponent_values)
            if opponent_values[0] <= 0:
                break
        else:
            print("Inserta una de las opciones posibles")
            time.sleep(0.5)
            continue

    time.sleep(0.5)

    #Turno del oponente
    x = random.choice(opponent_attacks)
    print("El oponente usó " + x)
    player_values = attack(attack_values[x], player_values)
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