n = int(input())

for _ in range(n):
    num = int(input())
    data = ""

    for i in range(1, num + 1):
        data += str(i)

    res = [0] * 10


    for s in data:
        res[int(s)] += 1

    print(' '.join(map(str, res)))
