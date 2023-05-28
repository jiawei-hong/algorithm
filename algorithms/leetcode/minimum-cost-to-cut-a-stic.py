class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        cuts = [0] + sorted(cuts) + [n]
        
        
        def dp(l, r):
            if (l,r) in memo:
                return memo[(l, r)]
            
            if r - l == 1:
                return 0
            
            find_min = 2 ** 31 - 1
            
            for i in range(l+1,r):
                n1 = dp(l,i) +  dp(i,r) + cuts[r] - cuts[l]
                
                find_min = min(find_min, n1)
                
            memo[(l,r)] = find_min
                
            
            return find_min
        
        return dp(0, len(cuts) - 1)