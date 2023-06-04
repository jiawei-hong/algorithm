class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        v = [False] * n
        res = 0

        def dfs(i):
            v[i] = True

            for j in range(n):
                if isConnected[i][j] and not v[j]:
                    dfs(j)

        for i in range(n):
            if not v[i]:
                res += 1
                dfs(i)

        return res