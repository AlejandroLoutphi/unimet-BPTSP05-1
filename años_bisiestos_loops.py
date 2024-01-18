while True:
        year = input("Inserte un año entre 1900 y 2199\n")
        try:
            year = int(year)
        except:
            pass
        else:
            if(year >= 1900 and year <= 2199):
                break
        print("Inserte un año válido")

#Este loop hace lo mismo que años_bisiestos_std.py::18
#Pero en lugar de hacerlo en O(1), lo hace en O(n)...
leap_year_cnt = 0
for i in range(1900, year+1):
    is_leap_year = ((i%4 == 0) and (not (i%100 == 0) or (i%400 == 0)))
    leap_year_cnt += is_leap_year

if is_leap_year:
    is_leap_year_str = "SÍ"
else:
    is_leap_year_str = "NO"

print("El año " + is_leap_year_str + " fue bisiesto")

if leap_year_cnt == 1:
    print("Ha habido 1 año bisiesto desde 1900 hasta " + str(year)) 
else:
    print("Han habido " + str(leap_year_cnt) + " años bisiestos desde 1900 hasta " + str(year))