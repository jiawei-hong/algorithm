class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        h = cur

        for g in gain:
            cur += g
            h = max(h, cur)

        return h