class Solution:
    def numOfWays(self, nums: List[int]) -> int:
         mod = 10 ** 9 + 7

         def dfs(nums):
            n = len(nums)

            if n <= 2:
                return 1

            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]


            return dfs(left) * dfs(right) * comb(n - 1, len(right)) % mod

         return (dfs(nums) - 1) % mod