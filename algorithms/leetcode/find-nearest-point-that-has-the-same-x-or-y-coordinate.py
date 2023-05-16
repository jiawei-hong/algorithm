class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        m = float('inf')
        res = -1

        for i in range(len(points)):
            a,b = points[i]
            if a == x or b == y:
                diff = abs(a-x) + abs(b-y)

                if diff < m:
                    m = diff
                    res = i
        return res