class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = len(s)
        res = roman[s[-1]]

        for i in range(n-1):
            [n1, n2] = [roman[s[i]], roman[s[i+1]]]

            if n1 < n2:
                res -= n1
            else:
                res += n1

        return res