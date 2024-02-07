nums = {
    "0":"cero",
    "1":"una",
    "2":"dos",
    "3":"tres",
    "4":"cuatro",
    "5":"cinco",
    "6":"seis",
    "7":"siete",
    "8":"ocho",
    "9":"nueve",
    "U":"unidad",
    "D":"decena",
    "C":"centena",
    "M":"mil",
    "-":"negativo"
}

digits = input("Ingrese el número en dígitos:\n")
output = []
is_negative = False

if digits[0] == "-":
    is_negative = True
    digits = digits[1:]

if not digits.isnumeric() or int(digits) > 999999:
    print("Entrada inválida")
    quit()

if len(digits) > 3:
    thousands = digits[0:3]
    digits = digits[3:6]

    if len(digits) > 2:
        output.append(nums[thousands[-3]])
        output.append(" ")
        output.append(nums["C"])
        if int(thousands[-3]) > 1:
            output.append("s")
        output.append(", ")

    if len(digits) > 1:
        output.append(nums[thousands[-2]])
        output.append(" ")
        output.append(nums["D"])
        if int(thousands[-2]) > 1:
            output.append("s")
        output.append(", y ")

    output.append(nums[thousands[-1]])
    output.append(" ")
    output.append(nums["U"])
    if int(thousands[-1]) > 1:
        output.append("es")
    
    output.append(" ")
    output.append(nums["M"])
    output.append(", ")

if len(digits) > 2:
    output.append(nums[digits[-3]])
    output.append(" ")
    output.append(nums["C"])
    if int(digits[-3]) > 1:
        output.append("s")
    output.append(", ")

if len(digits) > 1:
    output.append(nums[digits[-2]])
    output.append(" ")
    output.append(nums["D"])
    if int(digits[-2]) > 1:
        output.append("s")
    output.append(", y ")

output.append(nums[digits[-1]])
output.append(" ")
output.append(nums["U"])
if int(digits[-1]) > 1:
    output.append("es")

output = "".join(output)
output = is_negative * (nums["-"] + " ") + output
output = output[0].upper() + output[1:]
print(output)