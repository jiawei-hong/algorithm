class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0

        for expected_height, height in zip(sorted(heights), heights):
            if expected_height != height:
                res += 1
        return res
