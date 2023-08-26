n = int(input())

for _ in range(n):
    raw = list(map(int, input().strip().split()))
    eggs = raw[1:raw[0] + 1]
    cashs = raw[1+raw[0]:1+raw[0]*2]
 
    res = 0

    for egg, cash in zip(eggs, cashs):
        res += egg * cash

    print(str(res))
