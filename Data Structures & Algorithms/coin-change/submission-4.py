class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(i):
            if i == 0:
                return 0
            res = 1e9
            for coin in coins:
                if i - coin >= 0:
                    res =  min(res, 1 + dp(i-coin))
            return res
        minCoins = dp(amount)
        return -1 if minCoins >= 1e9 else minCoins