import sys

for line in sys.stdin.readlines():
    [a, b, c] = list(map(int, line.split()))
    nums = sorted([a, b, c])

    unknown = nums[1] if (nums[0] + nums[1]) > nums[2] else nums[2]

    if unknown == a:
        print('A')
    elif unknown == b:
        print("B")
    else:
        print('C')
