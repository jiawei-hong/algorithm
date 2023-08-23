answers = list(map(int, input().split()))

n = int(input())

for _ in range(n):
    res = 0

    nums = list(filter(lambda x: x in answers, map(int, input().split())))

    print(len(nums))
