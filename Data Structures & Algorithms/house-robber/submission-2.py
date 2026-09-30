class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            rob_curr = nums[i] + dp(i+2) #Rob current house and the next house.
            skip_curr = dp(i+1) #Skip current house and rob the rest
            memo[i] = max(rob_curr, skip_curr)
            return memo[i]
        return dp(0)

