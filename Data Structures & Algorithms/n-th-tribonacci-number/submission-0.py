class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2

        def mem(x):
            if x == 1 or x== 2:
                return 1
            if x == 0:
                return 0
            if x in dp.keys():
                return dp[x]
            else:
                dp[x] = mem(x-1) + mem(x-2) + mem(x-3)
            return dp[x]
        return mem(n)