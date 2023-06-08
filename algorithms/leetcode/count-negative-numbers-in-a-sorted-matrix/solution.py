class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        N, COL_N = len(grid), len(grid[0])
        res = 0

        for row in range(N):
            l, r = 0, COL_N - 1

            while l <= r:
                mid = (l + r) // 2

                if grid[row][mid] < 0:
                    r -= 1
                else:
                    l += 1 

            res += COL_N - l
                

        return res