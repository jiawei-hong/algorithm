class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        

        def dfs(i):
            if i >= n:
                return 0

            if dp[i]:
                return dp[i]

            num, skip_count = questions[i]

            dp[i] = max(dfs(i+1), num + dfs(i+skip_count+1))

            return dp[i]
        return dfs(0)