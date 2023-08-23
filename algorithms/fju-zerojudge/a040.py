[a, b] = list(map(int, input().split(' ')))

res = 0

for y in range(a, b+1):
    y = int(y)

    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        res += 1

print(res)
