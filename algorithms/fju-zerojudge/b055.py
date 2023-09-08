import sys

for line in sys.stdin.readlines():
    if line == '0':
        break

    nums = list(map(int, line.split()))
    nums.sort()
    res = 0

    while len(nums) > 1:
        a, b = nums.pop(0), nums.pop(0)

        nums.append(a+b)
        nums.sort()
        res += a+b

    print(str(res))
