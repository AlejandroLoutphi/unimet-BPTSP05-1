anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]


        },
    "Spy × Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}
history = []

while True:
    print("\nSe encuentra en el menú principal")
    x = input("Puede\n1) Seleccionar una serie a ver\n2) Consultar el historial de vistos\n3) Salir\n")
    
    if x == '1':
        print("¿Qué serie desea ver?")
        x = input("Opciones:\n" + "\n".join(list(anime)) + "\n")
        if not x in list(anime):
            print("Entrada inválida")
            continue
        print("¿Qué temporada desea ver?")
        y = input("Opciones:\n" + "\n".join(list(anime[x])) + "\n")
        if not y in list(anime[x]):
            print("Entrada inválida")
            continue
        z = input("Opciones:\n" + ", ".join([(str(i) + ") "+ str(anime[x][y][i]["cap"])) for i in range(len(anime[x][y]))]) + "\n")
        z = int(z)
        if not z in range(len(anime[x][y])):
            print("Entrada inválida")
            continue
        print("Anime: " + str(x) + "\nTemporada: " + str(y) + "\nCapítulo: " + str(z) + "\nNombre: " + str(anime[x][y][z]["name"]) + "\nDuración: " + str(anime[x][y][z]["duration"]))
        history.append("Anime: " + str(x) + "\nTemporada: " + str(y) + "\nCapítulo: " + str(z) + "\nNombre: " + str(anime[x][y][z]["name"]) + "\nDuración: " + str(anime[x][y][z]["duration"]))
        
    elif x == '2':
        print("Historial:\n" + "\n\n".join([(str(i+1) + ")\n"+ str(history[i])) for i in range(len(history))]) + "\nLa cantidad de capítulos vistos es: " + str(len(history)))
    elif x == '3':
        quit()
    else:
        print("Debe insertar 1, 2 o 3")