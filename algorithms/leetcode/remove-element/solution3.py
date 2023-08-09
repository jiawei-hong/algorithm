class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            if nums[i] == val:
                res += 1
            elif res > 0:
                nums[i - res] = nums[i]

        return n - res