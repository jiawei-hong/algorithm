class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        mid = sum(cost) / 2
        cur = 0

        for base, cost in arr:
            cur += cost
            
            if cur >= mid:
                return sum(abs(base - n) * c for n, c in arr)
