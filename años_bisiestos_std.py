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

if year%4 and (year%100 or not year%400):
    is_leap_year_str = "NO"
else:
    is_leap_year_str = "SÍ"
print("El año " + is_leap_year_str + " fue bisiesto")

leap_year_cnt = str((year-1900)//4-(year-1900)//100+(year-1600)//400)

if leap_year_cnt == 1:
    print("Ha habido 1 año bisiesto desde 1900 hasta " + str(year)) 
else:
    print("Han habido " + str(leap_year_cnt) + " años bisiestos desde 1900 hasta " + str(year))