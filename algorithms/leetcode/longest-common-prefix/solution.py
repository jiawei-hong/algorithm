class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        mx, mn = min(strs), max(strs)
        cur = 0

        for i in range(min(len(mx),len(mn))):
            if mx[i] != mn[i]:
                break
            
            cur += 1

        return mn[:cur]