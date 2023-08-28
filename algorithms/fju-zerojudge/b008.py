n = int(input())

for _ in range(n):
    [p,r,t] = map(float, input().split())

    rr = r / 100
    x = p * (1 + rr/12) ** (12 * t)

    print(round(x))
