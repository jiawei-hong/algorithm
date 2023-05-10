class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.dp = [[0 for _ in range(n)] for _ in range(n)]

        self.dfs(0,0,1,False)

        return self.dp

    
    def dfs(self,i,j,num,isUp):
        if i < 0 or j < 0 or i >= len(self.dp) or j >= len(self.dp[0]) or self.dp[i][j] != 0:
            return

        self.dp[i][j] = num

        num += 1

        if isUp:
            self.dfs(i-1,j,num,True)
        
        self.dfs(i,j+1,num,False)
        self.dfs(i+1,j,num,False)
        self.dfs(i,j-1,num,False)
        self.dfs(i-1,j,num,True)