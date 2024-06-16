class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        res = set()

        for i in range(n):
            for j in range(n):
                if i != j:
                    if (hours[i] + hours[j]) % 24 == 0:
                        res.add((min(i, j), max(i, j)))
        return len(res)
