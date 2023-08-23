[a, b] = list(map(int, input().split(' ')))

res = 0

a = a if a % 2 == 0 else a + 1
b = b if b % 2 == 0 else b - 1

print((b-a) // 2 + 1)
