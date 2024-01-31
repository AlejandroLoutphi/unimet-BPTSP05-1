nums = {
    "0": "X",
    "1": "1",
    "2": "11",
    "3": "111",
    "4": "1111",
    "5": "11111",
    "6": "111111",
    "7": "1111111",
    "8": "11111111",
    "9": "111111111",
}
x = input("Inserte un numero\n")
try:
    int(x)
except:
    quit()
out = []

for i in range(len(x)):
    out.append(nums[x[i]])
print("0".join(out))