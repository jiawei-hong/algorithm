from collections import Counter

n = int(input())


for _ in range(n):
    counter = Counter(input().split())

    print(counter.most_common()[0][1])
