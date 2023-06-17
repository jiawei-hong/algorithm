class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {}

        arr2.sort()

        def dfs(i,prev):
            if i == len(arr1): return 0

            if (i, prev) in dp:
                return dp[(i,prev)]

            costs = inf

            if arr1[i] > prev:
                costs = dfs(i+1, arr1[i])

            idx = bisect.bisect_right(arr2, prev)

            if idx < len(arr2):
                costs = min(costs, 1 + dfs(i+1, arr2[idx]))

            dp[(i,prev)] = costs

            return costs

        res = dfs(0, -1)

        return res if res < inf else -1