def input_to_posfloat(prompt):
    while True:
        input_string = input(prompt)
        try:
            result = float(input_string)
        except:
            print("Inserte un número válido")
        else:
            if(result > 0):
                return result
            else:
                print("Inserte un número válido")

arepa = input_to_posfloat("Cual seria el volumen de una arepa (tazas)? Recomendado: 0.7: ")
agua = input_to_posfloat("Cantidad de agua (tazas): ")
aceite = input_to_posfloat("Cantidad de aceite (cuharadas): ")  / 16
harina = input_to_posfloat("Cantidad de harina (tazas): ")
sal = input_to_posfloat("Cantidad de sal (cucharaditas): ") / 48
total = agua + aceite + harina + sal

print("El volumen total de arepas es " + str(total) + " tazas")
print("Se podrían hacer " + str(int(total // arepa)) + " arepas")

sobras = total % arepa
if sobras == 0:
    print("No sobraría nada. ¡Bien hecho!")
else:
    print("Sobrarían " + str(sobras) + " tazas")