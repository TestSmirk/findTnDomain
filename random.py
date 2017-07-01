a = list(range(1, 10))
b = []
for x in a:
    for y in a:
        for z in a:
            if x > y > z:
                b.append(str(x) + '*' + str(y) + '*' + str(z))
for h in range(len(b)):
    for i in range(len(b)):
        for j in range(len(b)):
            if eval(b[h]) == eval(b[i]) == eval(b[j]):
                if h >= i >= j:
                    if b[h] != b[i] != b[j]:
                        print(b[h], b[i], b[j])
