import math

def input_to_float(prompt):
    while True:
        input_string = input(prompt)
        try:
            result = float(input_string)
        except:
            print("Inserte un número válido")
        else:
            return result

print("Se resolverá una ecuación de la forma ax^2 + bx + c = 0")

a = input_to_float("Inserte el valor de \'a\'\n")
b = input_to_float("Inserte el valor de \'b\'\n")
c = input_to_float("Inserte el valor de \'c\'\n")

determinant = b*b - 4*a*c

if determinant < 0:
    print("No hay solución real a la cuadrática propuesta")
elif determinant == 0:
    Vx = -b/(2*a)
    print("La única solucuón real es " + str(Vx))
else:
    Vx = -b/(2*a)
    half_sqrt_determiant = math.sqrt(determinant)/2
    x1 = Vx + half_sqrt_determiant
    x2 = Vx - half_sqrt_determiant
    print("La primera solución es " + str(x1))
    print("La segunda solución es " + str(x2))