import random
import time

#Inicialización; parámetros de los ataques
player_HP = 100
opponent_HP = 100
player_defense = 100
opponent_defense = 100
opponent_starts = random.randrange(0, 1+1)

attack_damage = {
    "malicioso": 0, 
    "placaje": -35, 
    "ascuas": -10,
    "látigo": 0,
    "pistola de agua": -40
}
attack_defense = {
    "malicioso": -10, 
    "placaje": 0, 
    "ascuas": 0,
    "látigo": -10, 
    "pistola de agua": 0
}
attack_message = {
    "malicioso": None, 
    "placaje": None, 
    "ascuas": "No fue muy efectivo",
    "látigo": None, 
    "pistola de agua": "Fue super efectivo"
}

#Main loop
while player_HP > 0 and opponent_HP > 0:
    if opponent_starts == 0:
        #Tu turno
        x = input("Opciones: (Malicioso, Placaje, Ascuas)\nAtaque:\n")
        x = x.lower()
    
        if x in ["malicioso", "placaje", "ascuas"]:
            opponent_HP += attack_damage[x] * 100/opponent_defense
            opponent_defense += attack_defense[x]
            if opponent_defense <= 0:
                opponent_defense = 1
            if attack_message[x] is not None:
                time.sleep(0.5)
                print(attack_message[x])
        else:
            print("Inserta una de las opciones posibles")
            time.sleep(0.5)
            continue

    if opponent_HP <= 0:
        break

    time.sleep(0.5)

    #Turno del oponente
    x = random.choice(["látigo", "placaje", "pistola de agua"])
    print("El oponente usó " + x)
    player_HP += attack_damage[x] * 100/player_defense
    player_defense += attack_defense[x]
    if player_defense <= 0:
        player_defense = 1
    if attack_message[x] is not None:
        time.sleep(0.5)
        print(attack_message[x])

    time.sleep(0.5)
    opponent_starts = 0

#Fin de la batalla
time.sleep(0.5)
if player_HP <= 0:
    print("Has perdido")
else:
    print("Has ganado")