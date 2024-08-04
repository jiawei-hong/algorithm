class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans, n = 0, len(nums)
        mod = 10**9 + 7
        sorted_subarray_sum = sorted(
            [sum(nums[i : j + 1]) for i in range(n) for j in range(i, n)]
        )
        return sum(sorted_subarray_sum[left - 1 : right]) % mod
