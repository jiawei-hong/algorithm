class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i, diff] = dp.get((j, diff), 1) + 1

        return max(dp.values())