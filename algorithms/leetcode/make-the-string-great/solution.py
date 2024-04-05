class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            stack.append(c)
            if (
                len(stack) >= 2
                and stack[-1] != stack[-2]
                and stack[-1].lower() == stack[-2].lower()
            ):
                stack.pop()
                stack.pop()

        return "".join(stack)
