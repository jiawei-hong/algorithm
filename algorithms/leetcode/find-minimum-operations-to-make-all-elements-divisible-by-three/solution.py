class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        return sum([1 for i in range(n) if nums[i] % 3 != 0])
