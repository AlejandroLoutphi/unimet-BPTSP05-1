select = []
artist = [
    {
        "nombre": "Dimitri Thivaios y Michael Thivaios",
        "pseudonimo": "Dimitri Vegas & Like Mike",
        "estilos": ["Big Room House", "EDM", "Progressive House", "Future Bass"],
        "tarifaXminuto": 45,
        "escenarioRequerido": "RaveCage",
        "Reputacion": 9.5
    },{
        "nombre": "Tim Bergling",
        "pseudonimo": "Avicci (Zombie)",
        "estilos": ["Dance electrónica", "Electro House", "Progressive House"],
        "tarifaXminuto": 60,
        "escenarioRequerido": "Ultra Music",
        "Reputacion": 7.8
    },{
    },{
        "nombre": "Martijn Gerard Garritsen",
        "pseudonimo": "Martin Garrix",
        "estilos": ["Big Room House", "Electro", "EDM", "Progressive House", "Future Bass"],
        "tarifaXminuto": 45,
        "escenarioRequerido": "MainStage",
        "Reputacion": 9.8,
    },{
        "nombre": "Tijs Michiel Verwest",
        "pseudonimo": "Tiesto",
        "estilos": ["Big Room House", "Progressive House", "Dubstep", "EDM"],
        "tarifaXminuto": 20,
        "escenarioRequerido": "Mystery",
        "Reputacion": 7.5
    },{
        "nombre": "Nick van de Wall",
        "pseudonimo": "AfroJack",
        "estilos": ["Future Bass", "Progressive House", "Dubstep", "Electro House", "EDM"],
        "tarifaXminuto": 37,
        "escenarioRequerido": "Electrons",
        "Reputacion": 8.5
    },{
        "nombre": "Pierre David Guetta",
        "pseudonimo": "David Guetta",
        "estilos": ["Future Bass", "Progressive House", "EDM", "Electro House", "French House"],
        "tarifaXminuto": 50,
        "escenarioRequerido": "LastStage",
        "Reputacion": 9.65
    },{
        "nombre": "Timothy Jude Smith",
        "pseudonimo": "Timmy Trumpet",
        "estilos": ["Electro House","Big Room House","Bounce"],
        "tarifaXminuto": 35,
        "escenarioRequerido": "UltraLight",
        "Reputacion": 8.2
    }
]

while True:
    #Menu principal
    inp = input("Desea:\n1) Selecionar orden de presentación\n2) Ver lista de participantes totales y datos\n3) Salir\n")
    if inp == "1":
        #Seleccionar orden de presentación
        for i in range(len(artist)):
            print(">> Artista " + str(i+1) + 
                  ":\n   Nombre: " + artist[i]['nombre'] + "(" + artist[i]["pseudonimo"] + 
                  ")\n   Estilos: [" + ", ".join(artist[i]["estilos"]) +
                  "]\n   Tarifa: " + str(artist[i]["tarifaXminuto"]) + 
                  "$ x minuto\n   Escenario Requerido: " + artist[i]["escenarioRequerido"] + 
                  "\n   Reputación: " + str(artist[i]["Reputacion"]) + "\n")
    elif inp == "2":
        #Ver lista de participants totales y datos
        print("lol")
    elif inp == "3":
        quit()
    else:
        print("Entrada inválida")