class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        
        def rec(n):
            if n == 0 or n == 1:
                return 1
            
            if n in dp:
                return dp[n]
            
            dp[n] = rec(n-1) + rec(n-2)
            
            return dp[n]
        
        return rec(n)
            
            
        