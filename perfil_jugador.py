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

age = input("¿Qué edad tienes?\n")

while True:
    try:
        age = int(age)
    except:
        print("Responde un número válido")
    else:
        if age > 0:
            break
        else:
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