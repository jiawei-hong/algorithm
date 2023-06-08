class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        
        for x in grid:
            for i in x:
                if i < 0: count += 1
        return count