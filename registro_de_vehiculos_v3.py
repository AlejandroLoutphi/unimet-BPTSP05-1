#Clases genérica para todos los vehículos
class Seller:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return ("\nNombre del vendedor: " + self.name + "\nDirección del vendedor: " + self.address)

class Vehicle:
    minyear = -float('inf')
    maxyear = 2024
    str_name = "vehicle"

    def __init__(self, brand, model, year, seller):
        self.brand = brand
        self.model = model
        self.year = year
        self.seller = seller
    def __str__(self):
        return ("Marca: " + self.brand + "\nModelo: " + self.model + "\nAño: " + str(self.year) + "Vendedor:" + str(self.seller))
    
#Clases "hijas" para distintos tipos de vehículos
class ColoredVehicle(Vehicle):
    def __init__(self, brand, model, year, seller, color):
        Vehicle.__init__(self, brand, model, year, seller)
        self.color = color

class Car(ColoredVehicle):
    minyear = 1908
    str_name = "carro"

    def __str__(self):
        return ("Tipo: Carro\n" + Vehicle.__str__(self) + "\nColor: " + self.color)

class Boat(Vehicle):
    str_name = "barco"

    def __str__(self):
        return ("Tipo: Barco\n" + Vehicle.__str__(self))

class Plane(Vehicle):
    minyear = 1914
    str_name = "avion"

    def __str__(self):
        return ("Tipo: Avión\n" + Vehicle.__str__(self))

#2 funciones para distintos tipos de inputs
def input_list_element(prompt, options):
    while True:
        x = input(prompt)
        x = x.lower()
        if x in options: return x
        print("Seleccione una de las opciones posibles")

def input_int(prompt, min=-float("inf"), max=float("inf")):
    while True:
        x = input(prompt)
        try: x = int(x)
        except:
            print("Seleccione una de las opciones posibles")
            continue
        if x > min and x < max: return x
        elif (not min == -float("inf")) and (not max == float("inf")): print("El número debe estar entre " + str(min) + " y " + str(max))
        elif not min == -float("inf"): print("El número debe ser mayor a " + str(min))
        else: print("El número debe ser menor a " + str(max))

#Función en la que el usuario añade un vehículo a una lista    
def add_vehicle(vehicles: list):
    vehicle_types = [Car, Boat, Plane]
    vehicle_strs = [i.str_name for i in vehicle_types]

    input_str = input_list_element(
        "¿Qué vehículo desea registrar?\nOpciones: Carro, Barco, Avion\n",
        vehicle_strs)
    input_type = vehicle_types[vehicle_strs.index(input_str)]

    brand = input("¿Cuál es la marca del " + input_str + "?\n")
    model = input("¿Cuál es el nombre del modelo del " + input_str + "?\n")
    year = input_int("¿En qué año se introdujo el " + input_str + " al mercado?\n", input_type.minyear, input_type.maxyear)
    seller_name = input("¿Qué concesionario vendió el " + input_str + "?\n")
    seller_address = input("¿Cuál es la dirección del " + input_str + "?\n")
    seller = Seller(seller_name, seller_address)
    if issubclass(input_type, ColoredVehicle):    
        color = input_list_element(
            "¿De qué color es el " + input_str + "?\n",
            ["rojo", "naranja", "amarillo", "verde", "turquesa", "azul", "indigo", "cian", "morado", "rosado", "marron", "blanco", "gris", "negro"])
        vehicles.append(input_type(brand, model, year, seller, color))
    else:
        vehicles.append(input_type(brand, model, year, seller))
    print("El vehículo ha sido añadido")

#Función que lista todos los vehículos en una lista
def print_vehicles(vehicles):
    for i in range(len(vehicles)):
        print("\nVehículo " + str(i+1))
        print(str(vehicles[i]))

#Lista en la que se van a guardar todos los vehículos registrados
vehicles = []

#Inicialización de 2 objetos distintos de cada tipo
#No tengo ni idea si estos modelos son reales o no
vehicles.append(Car("Ford", "F-150", 2022, Seller("Genérico", "Caracas"), "gris"))
vehicles.append(Car("Toyota", "Corolla", 2016, Seller("motoristas?", "N/A"), "azul"))
vehicles.append(Boat("Beneteau", "Super Air Nautique", 1999, Seller("Attlanttic", "Florida")))
vehicles.append(Boat("Sea Ray", "Sweetwater", 2009, Seller("Bermuda", "Caribbean")))
vehicles.append(Plane("Boeing", "737 Max", 2002, Seller("DiamondShare", "California?")))
vehicles.append(Plane("Airbus", "A380", 2011, Seller("OurPlane", "Bancarrota")))

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