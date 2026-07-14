class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n,m = len(s), len(t)

        dp = [[-1] * m for _ in range(n)]

        def mem(i,j):
            if i == n:
                return True
            if j == m:
                return False
            if dp[i][j] != -1:
                return dp[i][j] == 1
            if s[i] == t[j]:
                dp[i][j] = 1 if mem(i+1, j+1) else 0
            else:
                dp[i][j] = 1 if mem(i, j+1) else 0
            return dp[i][j] == 1
        return mem(0,0)