x = [158,400,789,9926315,1634, 54748,200,4843, 481846, 48472,999, 93084, 24678050, 370,6, 100,89,78914,5161,1231,1515,3574,15731,4748743,848,1513,4545,657,25,987,50,47825,456,456,783, 1741725,88593477,48,111,121,28,777,401,412,214,369887,456,6664561,12,95,402,403,407,100,200,300,400,500,664,648,698,987,7,119, 2467, 149, 377, 9474, 548834, 153, 7, 9, 92727, 8208, 4210818, 407,487]
counts = {
    "afortunados": 0,
	"narcisistas": 0,
	"Otros": 0 # Para cuando no sea ninguno de los anteriores
}
out = []

for i in x:
    nar_sum = [int(a)**len(str(i)) for a in str(i)]
    nar_sum = sum(nar_sum)
    if nar_sum == i:
        counts["narcisistas"] += 1
        out.append("X")
        continue
    
    factor_sum = i
    for _ in range(100):
        if factor_sum == 6 or factor_sum == 28 or factor_sum == 496 or factor_sum == 8128 or factor_sum == 33550336 or factor_sum == 8589869056 or factor_sum == 137438691328:
            print("A" + str(i) + "P" + str(factor_sum))
            counts["afortunados"] += 1
            out.append("\n")
            break
        prev_factor_sum = factor_sum
        factor_sum = 1
        for j in range(2, prev_factor_sum):
            if prev_factor_sum%j == 0:
                factor_sum += j
                
    if not (factor_sum == 6 or factor_sum == 28 or factor_sum == 496 or factor_sum == 8128 or factor_sum == 33550336 or factor_sum == 8589869056 or factor_sum == 137438691328):
        counts["Otros"] += 1
        out.append(" ")
print("".join(out))
print(counts)