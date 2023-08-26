n = int(input())


for _ in range(n):
    raw = input().strip().split()
    res = 0

    for s in raw:
        if len(s) >= 10:
            res += 1

    print(res)
