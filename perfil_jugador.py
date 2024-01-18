while True:
    gender = input("¿Eres chico o chica?\n")
    gender = gender.lower()

    if gender == "chico":
        x = 'o'
    elif gender == "chica":
        x = 'a'
    else:
        print("Responde \"chico\" o \"chica\"")
        continue
    break
print("Bienvenid" + x + " al mundo de los Pokémon")

while True:
    age = input("¿Qué edad tienes?\n")
    try:
        age = int(age)
    except:
        pass
    else:
        if age > 0:
            break
    print("Responde un número válido")

if age < 10:
    print("No tienes edad para ser entrenador" + 'a'*(x=='a'))
    quit()
else:
    print("Vamos!")

region = input("Necesitarás un compañero de viaje.\n" +
               "En qué región te encuentras?\n" +
               "(Sugerencia: Kanto)\n")
if region.lower() == "kanto" and x == 'o':
    print("Tu compañera de viaje es Misty")
else:
    print("Tu compañero de viaje es Brock")

while True:
    tipo = input("¿Qué tipo de Pokémon quieres para empezar?\n")
    tipo = tipo.lower()

    if tipo == "agua":
        print("Tu starter es Oshawott")
    elif tipo == "fuego":
        print("Tu starter es Cyndaquil")
    elif tipo == "planta":
        print("Tu starter es Rowlet")
    else:
        print("Responde agua, fuego o planta")
        continue
    break