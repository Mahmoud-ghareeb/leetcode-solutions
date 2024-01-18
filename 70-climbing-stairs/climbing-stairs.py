class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        dp_1, dp_2 = 1, 2
        sol = 0
        for i in range(3, n+1):
            sol = dp_1 + dp_2
            dp_1 = dp_2
            dp_2 = sol

        return sol
            
        