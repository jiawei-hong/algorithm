n = int(input())

for _ in range(n):
    [a, b, c] = list(map(int, input().split(' ')))

    if a == b == c:
        print('Yes')
    else:
        print('No')
