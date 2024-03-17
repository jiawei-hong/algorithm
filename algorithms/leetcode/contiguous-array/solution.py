class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {0: -1}
        n = len(nums)
        count = 0
        ans = 0

        for i in range(n):
            count = count + (-1 if nums[i] == 0 else 1)
            if count in hash_map:
                ans = max(ans, i - hash_map[count])
            else:
                hash_map[count] = i
        return ans
