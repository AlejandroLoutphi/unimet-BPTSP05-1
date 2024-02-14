#Clases representando tipos de vehículos (son todos casi iguales por ahora)
class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    def print_attributes(self):
        print("Marca: " + self.brand)
        print("Modelo: " + self.model)
        print("Color: " + self.color)
        print("Año: " + str(self.year))

class Boat:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def print_attributes(self):
        print("Marca: " + self.brand)
        print("Modelo: " + self.model)
        print("Año: " + str(self.year))

class Plane:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def print_attributes(self):
        print("Marca: " + self.brand)
        print("Modelo: " + self.model)
        print("Año: " + str(self.year))

#2 funciones para distintos tipos de inputs
def input_list_element(prompt, options):
    while True:
        x = input(prompt)
        x = x.lower()
        if x in options: return x
        print("Seleccione una de las opciones posibles")

def input_int(prompt, min=None, max=None):
    while True:
        x = input(prompt)
        try: x = int(x)
        except:
            print("Seleccione una de las opciones posibles")
            continue
        if (min is None or x > min) and (max is None or x < max): return x
        elif (not min is None) and (not max is None): print("El número debe estar entre " + str(min) + " y " + str(max))
        elif not min is None: print("El número debe ser mayor a " + str(min))
        else: print("El número debe ser menor a " + str(max))

#Función en la que el usuario añade un vehículo a una lista    
def add_vehicle(vehicles: list):
    x = input_list_element(
        "¿Qué vehículo desea registrar?\nOpciones: Carro, Barco, Avion\n",
        ["carro", "barco", "avion"])

    if x == "carro":
        brand = input("¿Cuál es la marca del carro?\n")
        model = input("¿Cuál es el nombre del modelo del carro?\n")
        color = input_list_element(
            "¿De qué color es el carro?\n",
            ["rojo", "naranja", "amarillo", "verde", "turquesa", "azul", "indigo", "cian", "morado", "rosado", "marron", "blanco", "gris", "negro"])
        year = input_int("¿En qué año se introdujo el carro al mercado?\n", 1908, 2024)
        vehicles.append(Car(brand, model, color, year))
    elif x == "barco":
        brand = input("¿Cuál es la marca del barco?\n")
        model = input("¿Cuál es el nombre del modelo del barco?\n")
        year = input_int("¿En qué año se introdujo el barco al mercado?\n", None, 2024)
        vehicles.append(Boat(brand, model, year))
    elif x == "avion":
        brand = input("¿Cuál es la marca del avión?\n")
        model = input("¿Cuál es el nombre del modelo del avión?\n")
        year = input_int("¿En qué año se introdujo el avión al mercado?\n", 1914, 2024)
        vehicles.append(Plane(brand, model, year))
    print("El vehículo a sido añadido")

#Función que lista todos los vehículos en una lista
def print_vehicles(vehicles):
    for i in range(len(vehicles)):
        print("\nVehículo " + str(i+1))
        if type(vehicles[i]) is Car:
            print("Tipo: Carro")
            vehicles[i].print_attributes()
        elif type(vehicles[i]) is Boat:
            print("Tipo: Barco")
            vehicles[i].print_attributes()
        elif type(vehicles[i]) is Plane:
            print("Tipo: Avión")
            vehicles[i].print_attributes()

#Lista en la que se van a guardar todos los vehículos registrados
vehicles = []

#Inicialización de 2 objetos distintos de cada tipo
#No tengo ni idea si estos modelos son reales o no
vehicles.append(Car("Ford", "F-150", "gris", 2022))
vehicles.append(Car("Toyota", "Corolla", "azul", 2016))
vehicles.append(Boat("Beneteau", "Super Air Nautique", 1999))
vehicles.append(Boat("Sea Ray", "Sweetwater", 2009))
vehicles.append(Plane("Boeing", "737 Max", 2002))
vehicles.append(Plane("Airbus", "A380", 2011))

#Inicio de parte interactiva del programa
print("Bienvenido al sistema de registro de vehículos")

while True:
    x = input_list_element(
        "\n¿Qué desea hacer?\n1) Registrar un vehículo\n2) Ver vehículos registrados\n3) Salir\n",
        ["1", "2", "3"]
    )
    if x == "1": add_vehicle(vehicles)
    elif x == "2": print_vehicles(vehicles)
    else: quit()