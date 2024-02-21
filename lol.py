def sum(x):
    #x = [0] + x + [0]
    out = []
    #av = int(len(x)/2)

    for s in range(len(x)):
        a = []
        b = []
        
        for i in range(0, s):
            a.append(x[i])
        for i in range(s+1, len(x)):
            b.append(x[i])
        print(a)
        print(b)
        n = 0
        m = 0
        for i in a:
            n += i
        for i in b:
            m += i
        print(n)
        print(m)
        out.append(m+n)
    return out


x = [1, 2, 3, 9, 5, 7]
sum(x)
print(sum(x))