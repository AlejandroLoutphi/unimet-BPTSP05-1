nums = []
print("Escriba elementos de la lista.\nEscriba una letra para parar.")
while True:
    num = input("")
    try:
        num = int(num)
    except:
        if nums == []:
            print("Escriba un numero válido")
        else:
            break
    else:
        nums.append(num)
        
equal_pairs = 0

for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):
        equal_pairs += 1*(nums[i] == nums[j])
print("La cantidad de pares iguales en la lista es: " + str(equal_pairs))