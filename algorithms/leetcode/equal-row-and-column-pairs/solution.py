class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        record = defaultdict(int)

        for row in grid:
            record[str(row)] += 1

        for i in range(len(grid[0])):
            col = [grid[j][i] for j in range(len(grid))]
            res += record[str(col)]

        return res