nums = list(map(int, input().split()))

p = sum(nums) // 2

print(p * (p-nums[0]) * (p-nums[1]) * (p-nums[2]))
