class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s_n = len(s)
        goal_n = len(goal)

        if s == goal and len:
            return True


        diffs = [i for i in range(len(s)) if s[i] != goal[i]]

        diffs_n = len(diffs)

        if diffs_n != 2:
            return False

        return s_n == goal_n and s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]