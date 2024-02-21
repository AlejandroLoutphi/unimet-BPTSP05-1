#Clase de vehiculo, vendedor y venta
class Vehicle:
    def __init__(self, name, type, brand, model, year, color):
        self.name = name
        self.type = type 
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    def __str__(self):
        return ("Nombre: " + self.name + "\nMarca: " + self.brand + "\nTipo: " + self.type + "\nModelo: " + self.model + "\nAño: " + str(self.year) + "Color:" + self.color)
    
class Seller:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return ("Nombre: " + self.name + "\nDirección: " + self.address)

class Sale:
    def __init__(self, vehicle, seller, year):
        self.vehicle = vehicle
        self.seller = seller
        self.year = year
        
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
        elif (min != -float("inf")) and (max != float("inf")): print("El número debe estar entre " + str(min) + " y " + str(max))
        elif not min == -float("inf"): print("El número debe ser mayor a " + str(min))
        else: print("El número debe ser menor a " + str(max))

#Función en la que se registra una venta    
def register_sale(vehicles: list, sellers: list, sales: list):
    vehicle = input_list_element("¿Cuál es el vehíuclo a ser vendido?\n", str([i.name for i in vehicles]))
    vehicle = vehicles[[i.name for i in vehicles].index(vehicle)]
    seller = input_list_element("¿Cuál fue el vendedor del vehículo?\n", str([i.name for i in sellers]))
    seller = sellers[[i.name for i in sellers].index(seller)]
    year = input_int("¿En qué año se ha vendido el vehículo?\n", max=2024)
    sales.append(Sale(vehicle, seller, year))
    print("La venta ha sido registrada")

#Función que listan todas las ventas registradas 
def print_registry(sales: list):
    for i in range(len(sales)):
        print("\n\nVenta " + str(i+1))
        print("\nVehículo: ")
        print(str(sales[i].vehicle))
        print("\nVendedor: ")
        print(str(sales[i].seller))
        print("\nAño de realización de la venta: ")
        print(str(sales[i].year))

#Listas en las que se van a guardar todos los vehículos, vendedores y ventas registrados
vehicles = []
sellers = []
sales = []

#Inicialización de varios vehiculos y vendedores
vehicles.append(Vehicle("1", "carro", "Ford", "F-150", 2022, "gris"))
vehicles.append(Vehicle("2", "carro", "Toyota", "Corolla", 2016,  "azul"))
vehicles.append(Vehicle("3", "barco", "Beneteau", "Super Air Nautique", 1999, "blanco"))
vehicles.append(Vehicle("4", "barco", "Sea Ray", "Sweetwater", 2009, "rojo"))
vehicles.append(Vehicle("5", "avion", "Boeing", "737 Max", 2002, "cian"))
vehicles.append(Vehicle("6", "avion", "Airbus", "A380", 2011, "verde"))
sellers.append(Seller("attlantic", "Florida"))
sellers.append(Seller("t-rex", "Caracas"))
sellers.append(Seller("zippy", "Madrid"))
sellers.append(Seller("xtreme motors", "California"))
sellers.append(Seller("breeze auto", "Bogota"))
#Inicio de parte interactiva del programa
print("Bienvenido al sistema de registro de vehículos")

while True:
    x = input_list_element(
        "\n¿Qué desea hacer?\n1) Registrar una venta\n2) Ver ventas registradas\n3) Salir\n",
        ["1", "2", "3"]
    )
    if x == "1": register_sale(vehicles, sellers, sales)
    elif x == "2": print_registry(sales)
    else: quit()