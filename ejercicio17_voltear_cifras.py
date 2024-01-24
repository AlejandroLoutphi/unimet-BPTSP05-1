while True:
    num = input("Escriba el numero a voltear.\n")
    try:
        int(num)
    except:
        print("Escriba un numero válido")
    else:
        break
flipped_num = ""

for i in range(len(num)-1, 0-1, -1):
    flipped_num = flipped_num + num[i]
print("El número volteado es: " + flipped_num)