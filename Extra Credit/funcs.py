#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande y Ayah ZaherAlDeen

def input_list_elt(prompt: str, options: list, error: str = "Seleccione una de las opciones posibles") -> str:
    while True:
        x = input(prompt)
        x = x.lower()
        if x in options: return x
        print(error)

def input_posint(prompt: str) -> int:
    while True:
        try: x = int(input(prompt))
        except:
            print("Inserte un número válido")
            continue
        if x < 0:
            print("Inserte un número válido")
            continue
        return x