class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l = max(left, default=0)
        r = n - min(right, default=2**31)

        return max(l, r)
