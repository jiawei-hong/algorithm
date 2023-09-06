def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


primes = []
i = 2
while len(primes) < 1001:
    if isPrime(i):
        primes.append(i)

    i += 1

n = int(input())

for _ in range(n):
    num = int(input())

    print(str(primes[num-1]))
