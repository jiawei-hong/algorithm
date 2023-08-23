k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    n = 1

    while a**n <= b:
        n += 1

    print(n - 1)
