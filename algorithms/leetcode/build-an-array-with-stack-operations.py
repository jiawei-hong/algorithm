class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        seem = set(target)

        for i in range(1, target[-1] + 1):
            res.append('Push')

            if i not in seem:
                res.append('Pop')

        return res