from collections import Counter

n = int(input())
res = 0


for i in range(n):
    count_for_solution = list(map(lambda x: int(x), input().split(' ')))
    counter = Counter(count_for_solution)

    if counter[1] >= 2:
        res += 1

print(res)


