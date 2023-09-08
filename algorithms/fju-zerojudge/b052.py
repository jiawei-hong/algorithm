import sys


def isPrime(n):
    if n % 2 == 0:
        return n == 2

    for i in range(3, n):
        if n % i == 0:
            return False

    return True


for line in sys.stdin.readlines():
    num = int(line)

    if num < 2:
        continue

    mn = mx = 0

    for i in range(0, num):
        if isPrime(i) and i > mn:
            mn = i

    i = num + 1

    while mx == 0:
        if isPrime(i) and i > mx:
            mx = i
        i += 1

    print(f'{mn} {mx}')
