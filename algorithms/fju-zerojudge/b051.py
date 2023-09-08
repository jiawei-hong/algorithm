n = int(input())

for _ in range(n):
    s = ''.join(input().split())
    n = len(s)
    a, b = [], []

    for i in range(0, n, 2):
        a.append(s[i])

        if i + 1 < n:
            b.append(s[i+1])

    print(''.join((a+b)).upper())
