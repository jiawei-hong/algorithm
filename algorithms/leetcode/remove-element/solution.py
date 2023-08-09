class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1

        return res