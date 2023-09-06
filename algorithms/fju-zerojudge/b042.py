from collections import Counter

money = int(input())
n = int(input())
counter = Counter(map(int, input().split()))

for k, v in counter.items():
    res = money*v
    print(f'{k}: {money} * {v} = {res}')
