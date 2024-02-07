penta = [[45,78,65],[12,35,70],[51,3,105],[22,12,85]]
for i in penta:
    for a in i:
        penta[penta.index(i)][penta[penta.index(i)].index(a)] = a*(3*a-1)/2
print(penta)