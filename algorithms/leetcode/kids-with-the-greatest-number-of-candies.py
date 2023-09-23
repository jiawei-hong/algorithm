class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        mx = max(candies)
        res = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= mx:
                res[i] = True

        return res
