class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        nx = cur = releaseTimes[0]
        res = defaultdict(list)
        res[cur].append(keysPressed[0])

        for i in range(1, n):
            t = releaseTimes[i] - cur
            nx = max(nx, t)
            res[t].append(keysPressed[i])
            cur = releaseTimes[i]

        sorted_res = sorted(res[nx])
        return sorted_res[-1]
