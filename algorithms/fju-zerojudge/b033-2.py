n = int(input())

for _ in range(n):
    m, mx = map(int, input().split())
    n = 0
    res = 0

    while res + (n * m + 1) <= mx:
        res += n*m+1
        n += 1

    last_term = (n-1) * m + 1
    print(last_term)
