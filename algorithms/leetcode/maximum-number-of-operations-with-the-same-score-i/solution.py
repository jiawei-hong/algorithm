class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans = 1
        num = nums[0] + nums[1]

        for i in range(2, len(nums)-1,2):
            if nums[i] + nums[i+1] == num:
                ans += 1
            else:
                break
        return ans
