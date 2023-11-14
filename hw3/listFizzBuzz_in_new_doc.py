

with open('list.txt') as f, open('listFB.txt', 'w') as fw:
    for line in f:
        f, b, n = map(int, line.split())
        result = []

    for i in range(1, n+1):
        if not i % f and not i % b:
            result.append("FB")
        elif not i % f:
            result.append("F")
        elif not i % b:
            result.append("B")
        else:
            result.append(str(i))
    print(" ". join(result), file=fw)
fw.close()
