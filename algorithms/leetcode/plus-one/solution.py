class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[-1] += 1

        digits.reverse()

        for i in range(n):
            if digits[i] > 9:
                if i + 1 < n:
                    digits[i+1] += 1
                else:
                    digits.insert(n, 1)

                digits[i] %= 10
        digits.reverse()
        return digits