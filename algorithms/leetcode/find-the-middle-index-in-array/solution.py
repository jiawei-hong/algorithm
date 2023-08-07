class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumLeft = []
        sumRight = []

        for i in range(n):
            sumLeft.append(sum(nums[:i]))
            sumRight.append(sum(nums[i+1:]))

            if sumLeft[-1] == sumRight[-1]:
                return i

        return -1