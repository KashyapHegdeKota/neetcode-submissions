class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        
        def mem(x):
            # Base Cases given by the problem
            if x == 0:
                return 0
            if x == 1 or x == 2:
                return 1
            
            # Check memo
            if x in dp:
                return dp[x]
            
            # The correct formula: sum of the previous THREE terms
            dp[x] = mem(x-1) + mem(x-2) + mem(x-3)
            return dp[x]
            
        return mem(n)