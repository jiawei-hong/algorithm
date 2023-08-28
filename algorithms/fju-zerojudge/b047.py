n = int(input())

fib = [0,1]

for i in range(2, 1001):
    fib.append(fib[i-1]+fib[i-2])

def gcd(a,b):
    if b == 0:
        return a

    return gcd(b, a % b)

for _ in range(n):
    a,b = map(int, input().split())

    print(gcd(fib[a],fib[b]))
