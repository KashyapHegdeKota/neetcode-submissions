class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def mem(x):
            if x == 0: 
                return 0
            if x < 0:
                return -1
            if x in dp.keys():
                return dp[x] 
            res = float("inf")
            for coin in coins:
                rem = x - coin
                tmp = mem(rem)

                if tmp >= 0:
                    var = tmp +1
                    if var < res:
                        res = var
            dp[x] = -1 if res == float("inf") else res
            return dp[x]
        return mem(amount)
