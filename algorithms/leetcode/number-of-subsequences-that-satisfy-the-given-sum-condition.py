class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        n,res,m = len(nums), 0, 1000000007
        l,r = 0, n - 1

        while l <= r:
            if nums[l] + nums[r] <= target:
                res += pow(2, r-l, m)
                l += 1
            else:
                r -= 1

        return res % m