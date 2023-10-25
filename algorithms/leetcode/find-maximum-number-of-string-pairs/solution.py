class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set()
        res = 0

        for word in words:
            if word[::-1] in s:
                s.remove(word[::-1])
                res += 1
            else:
                s.add(word)

        return res
