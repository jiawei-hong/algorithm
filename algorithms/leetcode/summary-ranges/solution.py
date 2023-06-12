class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def helper(a:str, b:str) -> str:
            return str(a) if a == b else f'{a}->{b}'

        n = len(nums)

        if n == 0:
            return []

        res = []
        cur = 0

        while cur < n:
            record = nums[cur]

            while cur + 1 < n and nums[cur] + 1 == nums[cur + 1]:
                cur += 1

            res.append(helper(record, nums[cur]))

            cur += 1

        return res