class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = ''

        for i in range(0, n, k * 2):
            res += s[i:i+k][::-1] + s[i+k:i+(k*2)]

        return res
