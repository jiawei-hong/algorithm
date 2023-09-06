import math


def isPrime(n):
    if n % 2 == 0:
        return n == 2

    if n > 2:
        for i in range(3, math.floor(math.sqrt(n)), 2):
            if n % i == 0:
                return False

        return True

    return False


n = int(input())

for _ in range(n):
    num = int(input())
    is_prime = isPrime(num)

    print(f'{num}: ' + ('YES' if is_prime else 'NO'))
