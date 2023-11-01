class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(goal)

        for i in range(n):
            t = s[i+1:] + s[0:i+1]

            if t == goal:
                return True
        
        return False