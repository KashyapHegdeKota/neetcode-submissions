class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i >= len(nums):
                return 0
            rob_curr = nums[i] + dp(i+2) #Rob current house and the next house.
            skip_curr = dp(i+1) #Skip current house and rob the rest
            return max(rob_curr, skip_curr)
        return dp(0)
