[a, b] = list(map(int, input().split(' ')))
res = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        res += i

print(res)
