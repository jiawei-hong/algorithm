class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mx = 0
        count = defaultdict(int)

        for word in words:
            for c in word:
                count[c] += 1
                mx = max(mx, count[c])

        n = len(words)
        for val in count.values():
            if val % n != 0:
                return False

        return True
