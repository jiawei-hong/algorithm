class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b_x = bin(x)[2:]
        b_y = bin(y)[2:]

        if len(b_x) > len(b_y):
            b_y = ('0' * (abs(len(b_y) - len(b_x)))) + b_y
        else:
            b_x = ('0' * (abs(len(b_y) - len(b_x)))) + b_x

        res = 0

        for i in range(len(b_x)):
            if b_x[i] != b_y[i]:
                res += 1

        return res
