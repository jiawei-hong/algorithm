class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        parent_theses = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        keys = parent_theses.keys()

        for i in range(n):
            if s[i] in keys:
                stack.append(parent_theses[s[i]])
                continue

            if len(stack) == 0:
                return False

            check = stack.pop()

            if s[i] != check:
                return False

        return len(stack) == 0