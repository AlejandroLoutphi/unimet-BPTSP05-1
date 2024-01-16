while True:
    gender = input("¿Eres chico o chica?\n")

    if gender.lower() == "chico":
        x = 'o'
        break
    elif gender.lower() == "chica":
        x = 'a'
        break
    else:
        print("Responde \"chico\" o \"chica\"")
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