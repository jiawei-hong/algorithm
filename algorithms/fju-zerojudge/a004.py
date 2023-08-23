n = int(input())
res = 0
steamed_bun = list(map(int, input().split()))

for i, bun in enumerate(steamed_bun):
    res += bun * (i + 1)

print(str(res))
