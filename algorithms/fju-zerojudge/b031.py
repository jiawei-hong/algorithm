from collections import Counter

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    counter = Counter(nums)

    a = [k for k, v in counter.items() if v == 3]
    b = [k for k, v in counter.items() if v == 1]

    result = max(a) if a else max(b) if b else 0
    print(result)
