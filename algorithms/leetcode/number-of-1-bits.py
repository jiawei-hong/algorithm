class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(list(filter(lambda x: x == '1',list("{0:b}".format(n)))))