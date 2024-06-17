class Solution:
    def checkString(self, s: str) -> bool:
        flag = False

        for i in range(len(s)):
            if flag and s[i] == "a":
                return False

            if not flag and s[i] == "b":
                flag = True
        return True
