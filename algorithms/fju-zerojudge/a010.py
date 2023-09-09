
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    words = ''.join([input() for _ in range(n)])

    print(''.join([words[x-1] for x in list(map(int, input().split()))]))
