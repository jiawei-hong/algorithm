class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = sum(map(int, list(str(x))))

        return -1 if x % n != 0 else n
