class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]

        def find(n):
            while n != parent[n]:
                n = parent[n]

            return n 

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            parent[p2] = p1

            return 1

        res = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    res -= union(i,j)

        return res