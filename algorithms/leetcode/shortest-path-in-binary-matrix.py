class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        directions = [
            # tl, l, bl
            (-1, -1), (-1, 0), (-1, 1),
            # t,b
            (0, -1), (0, 1),
            # bl, r,br
            (1, -1), (1, 0), (1, 1)
        ]

        queue = [(0,0,1)]
        grid[0][0] = 1

        while queue:
            i,j,d = queue.pop(0)
            
            # is collision to the wall
            if i == n -1 and j == n -1:
                return d

            for x,y in directions:
                dx, dy = x+i,y+j

                if 0 <= dx < n and 0 <= dy < n and not grid[dx][dy]:
                    grid[dx][dy] = 1
                    queue.append((dx,dy,d+1))
        return -1