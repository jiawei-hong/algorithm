class Solution:
    def calc(self, n1, n2, symbol):
        if symbol == '+':
            return n1 + n2

        if symbol == '-':
            return n2 - n1

        if symbol == '*':
            return n1 * n2

        return int(n2/n1)

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if token not in '+-*/':
                nums.append(int(token))
            else:
                n1, n2 = nums.pop(), nums.pop()

                nums.append(self.calc(n1, n2, token))

        return nums[0]
