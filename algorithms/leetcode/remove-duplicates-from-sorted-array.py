class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        cur = 0
        
        for i in range(1, n):
            num = nums[i]
            
            if nums[cur] != num:
                cur += 1
                nums[cur] = num

        return cur + 1