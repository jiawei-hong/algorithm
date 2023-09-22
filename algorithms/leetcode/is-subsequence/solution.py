class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r = 0

        for i in range(len(t)):
            if r >= len(s): continue
            if t[i] == s[r]:
                r += 1
        return r == len(s)