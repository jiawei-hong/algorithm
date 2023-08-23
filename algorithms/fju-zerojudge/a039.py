import sys

res = 0

for line in sys.stdin.readlines():
    [a, b, c] = list(map(int, line.split(' ')))

    if a + b > c and b + c > a and c+a > b:
        res += 1

print(res)
