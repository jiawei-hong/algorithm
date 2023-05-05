class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = max_vowel = 0

        for i in range(len(s)):
            if i >= k:
                if s[i-k] in vowels:
                    res -= 1

            if s[i] in vowels:
                res += 1
            max_vowel = max(max_vowel, res)
            if max_vowel == k:
                return max_vowel
        return max_vowel
