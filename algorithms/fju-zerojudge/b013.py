n = int(input())


for _ in range(n):
    data  = int(input())
    num = 2
    res = []

    while data != 1:
        if data % num != 0:
            num += 1
            continue

        data //= num
        res.append(str(num))

    print(' '.join(res))
    
