class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        d = defaultdict(lambda: 0)

        for hour in hours:
            # hour = 30
            remain = hour % 24  # 6
            need = (24 - remain) % 24  # 18
            res += d[need]  # add we need hour
            d[remain] += 1  # update remain time

        return res
