class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'

        def getBinary(num):
            n = len(num) - 1
            res = 0

            for i in range(len(num) - 1, -1, -1):
                res += int(num[n-i]) * (2 ** i)
            return res

        sum_num = getBinary(a) + getBinary(b)
        res = ''

        while sum_num > 0:
            res = str(sum_num % 2) + res
            sum_num //= 2

        return res
