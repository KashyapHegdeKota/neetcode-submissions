class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: 
            return 1
        dp = {}
        dp[0] = 1
        
        def mem(n):
            if n < 0:
                return 0
            if n in dp.keys():
                return dp[n]
            else:
                dp[n] = mem(n-1) + mem(n-2)
            return dp[n]
        return mem(n)